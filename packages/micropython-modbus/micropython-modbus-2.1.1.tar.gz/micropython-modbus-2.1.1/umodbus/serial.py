#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

# system packages
from machine import UART
from machine import Pin
import struct
import time
import machine

# custom packages
from . import const as Const
from . import functions
from .common import Request
from .common import ModbusException
from .modbus import Modbus

# typing not natively supported on MicroPython
from .typing import List, Optional, Tuple, Union


class ModbusRTU(Modbus):
    """
    Modbus RTU client class

    :param      addr:        The address of this device on the bus
    :type       addr:        int
    :param      baudrate:    The baudrate, default 9600
    :type       baudrate:    int
    :param      data_bits:   The data bits, default 8
    :type       data_bits:   int
    :param      stop_bits:   The stop bits, default 1
    :type       stop_bits:   int
    :param      parity:      The parity, default None
    :type       parity:      Optional[int]
    :param      pins:        The pins as list [TX, RX]
    :type       pins:        List[int, int]
    :param      ctrl_pin:    The control pin
    :type       ctrl_pin:    int
    """
    def __init__(self,
                 addr: int,
                 baudrate: int = 9600,
                 data_bits: int = 8,
                 stop_bits: int = 1,
                 parity: Optional[int] = None,
                 pins: List[int, int] = None,
                 ctrl_pin: int = None):
        super().__init__(
            # set itf to Serial object, addr_list to [addr]
            Serial(uart_id=1,
                   baudrate=baudrate,
                   data_bits=data_bits,
                   stop_bits=stop_bits,
                   parity=parity,
                   pins=pins,
                   ctrl_pin=ctrl_pin),
            [addr]
        )


class Serial(object):
    def __init__(self,
                 uart_id: int = 1,
                 baudrate: int = 9600,
                 data_bits: int = 8,
                 stop_bits: int = 1,
                 parity=None,
                 pins: List[int, int] = None,
                 ctrl_pin: int = None):
        """
        Setup Serial/RTU Modbus

        :param      uart_id:     The ID of the used UART
        :type       uart_id:     int
        :param      baudrate:    The baudrate, default 9600
        :type       baudrate:    int
        :param      data_bits:   The data bits, default 8
        :type       data_bits:   int
        :param      stop_bits:   The stop bits, default 1
        :type       stop_bits:   int
        :param      parity:      The parity, default None
        :type       parity:      Optional[int]
        :param      pins:        The pins as list [TX, RX]
        :type       pins:        List[int, int]
        :param      ctrl_pin:    The control pin
        :type       ctrl_pin:    int
        """
        self._uart = UART(uart_id,
                          baudrate=baudrate,
                          bits=data_bits,
                          parity=parity,
                          stop=stop_bits,
                          # timeout_chars=2,  # WiPy only
                          # pins=pins         # WiPy only
                          tx=pins[0],
                          rx=pins[1]
                          )

        if ctrl_pin is not None:
            self._ctrlPin = Pin(ctrl_pin, mode=Pin.OUT)
        else:
            self._ctrlPin = None

        if baudrate <= 19200:
            # 4010us (approx. 4ms) @ 9600 baud
            self._t35chars = (3500000 * (data_bits + stop_bits + 2)) // baudrate
        else:
            self._t35chars = 1750   # 1750us (approx. 1.75ms)

    def _calculate_crc16(self, data: bytearray) -> bytes:
        """
        Calculates the CRC16.

        :param      data:        The data
        :type       data:        bytearray

        :returns:   The crc 16.
        :rtype:     bytes
        """
        crc = 0xFFFF

        for char in data:
            crc = (crc >> 8) ^ Const.CRC16_TABLE[((crc) ^ char) & 0xFF]

        return struct.pack('<H', crc)

    def _exit_read(self, response: bytearray) -> bool:
        """
        Return on modbus read error

        :param      response:    The response
        :type       response:    bytearray

        :returns:   State of basic read response evaluation
        :rtype:     bool
        """
        if response[1] >= Const.ERROR_BIAS:
            if len(response) < Const.ERROR_RESP_LEN:
                return False
        elif (Const.READ_COILS <= response[1] <= Const.READ_INPUT_REGISTER):
            expected_len = Const.RESPONSE_HDR_LENGTH + 1 + response[2] + Const.CRC_LENGTH
            if len(response) < expected_len:
                return False
        elif len(response) < Const.FIXED_RESP_LEN:
            return False

        return True

    def _uart_read(self) -> bytearray:
        """
        Read up to 40 bytes from UART

        :returns:   Read content
        :rtype:     bytearray
        """
        response = bytearray()

        for x in range(1, 40):
            if self._uart.any():
                # WiPy only
                # response.extend(self._uart.readall())
                response.extend(self._uart.read())

                # variable length function codes may require multiple reads
                if self._exit_read(response):
                    break
            time.sleep(0.05)

        return response

    def _uart_read_frame(self, timeout: Optional[int] = None) -> bytearray:
        """
        Read a Modbus frame

        :param      timeout:  The timeout
        :type       timeout:  Optional[int]

        :returns:   Received message
        :rtype:     bytearray
        """
        received_bytes = bytearray()

        # set timeout to at least twice the time between two frames in case the
        # timeout was set to zero or None
        if timeout == 0 or timeout is None:
            timeout = 2 * self._t35chars  # in milliseconds

        start_us = time.ticks_us()

        # stay inside this while loop at least for the timeout time
        while (time.ticks_diff(time.ticks_us(), start_us) <= timeout):
            # check amount of available characters
            if self._uart.any():
                # remember this time in microseconds
                last_byte_ts = time.ticks_us()

                # do not stop reading and appending the result to the buffer
                # until the time between two frames elapsed
                while time.ticks_diff(time.ticks_us(), last_byte_ts) <= self._t35chars:
                    # WiPy only
                    # r = self._uart.readall()
                    r = self._uart.read()

                    # if something has been read after the first iteration of
                    # this inner while loop (during self._t35chars time)
                    if r is not None:
                        # append the new read stuff to the buffer
                        received_bytes.extend(r)

                        # update the timestamp of the last byte being read
                        last_byte_ts = time.ticks_us()

            # if something has been read before the overall timeout is reached
            if len(received_bytes) > 0:
                return received_bytes

        # return the result in case the overall timeout has been reached
        return received_bytes

    def _send(self, modbus_pdu: bytes, slave_addr: int) -> None:
        """
        Send Modbus frame via UART

        If a flow control pin has been setup, it will be controller accordingly

        :param      modbus_pdu:  The modbus Protocol Data Unit
        :type       modbus_pdu:  bytes
        :param      slave_addr:  The slave address
        :type       slave_addr:  int
        """
        serial_pdu = bytearray()
        serial_pdu.append(slave_addr)
        serial_pdu.extend(modbus_pdu)

        crc = self._calculate_crc16(serial_pdu)
        serial_pdu.extend(crc)

        if self._ctrlPin:
            self._ctrlPin(1)

        self._uart.write(serial_pdu)

        if self._ctrlPin:
            while not self._uart.wait_tx_done(2):
                machine.idle()
            time.sleep_us(self._t35chars)
            self._ctrlPin(0)

    def _send_receive(self,
                      modbus_pdu: bytes,
                      slave_addr: int,
                      count: bool) -> bytes:
        """
        Send a modbus message and receive the reponse.

        :param      modbus_pdu:  The modbus Protocol Data Unit
        :type       modbus_pdu:  bytes
        :param      slave_addr:  The slave address
        :type       slave_addr:  int
        :param      count:       The count
        :type       count:       bool

        :returns:   Validated response content
        :rtype:     bytes
        """
        # flush the Rx FIFO
        self._uart.read()

        self._send(modbus_pdu=modbus_pdu, slave_addr=slave_addr)

        return self._validate_resp_hdr(response=self._uart_read(),
                                       slave_addr=slave_addr,
                                       function_code=modbus_pdu[0],
                                       count=count)

    def _validate_resp_hdr(self,
                           response: bytearray,
                           slave_addr: int,
                           function_code: int,
                           count: bool) -> bytes:
        """
        Validate the response header.

        :param      response:       The response
        :type       response:       bytearray
        :param      slave_addr:     The slave address
        :type       slave_addr:     int
        :param      function_code:  The function code
        :type       function_code:  int
        :param      count:          The count
        :type       count:          bool

        :returns:   Modbus response content
        :rtype:     bytes
        """
        if len(response) == 0:
            raise OSError('no data received from slave')

        resp_crc = response[-Const.CRC_LENGTH:]
        expected_crc = self._calculate_crc16(
            response[0:len(response) - Const.CRC_LENGTH]
        )

        if ((resp_crc[0] is not expected_crc[0]) or
                (resp_crc[1] is not expected_crc[1])):
            raise OSError('invalid response CRC')

        if (response[0] != slave_addr):
            raise ValueError('wrong slave address')

        if (response[1] == (function_code + Const.ERROR_BIAS)):
            raise ValueError('slave returned exception code: {:d}'.
                             format(response[2]))

        hdr_length = (Const.RESPONSE_HDR_LENGTH + 1) if count else \
            Const.RESPONSE_HDR_LENGTH

        return response[hdr_length:len(response) - Const.CRC_LENGTH]

    def read_coils(self,
                   slave_addr: int,
                   starting_addr: int,
                   coil_qty: int) -> List[bool]:
        """
        Read coils (COILS).

        :param      slave_addr:     The slave address
        :type       slave_addr:     int
        :param      starting_addr:  The coil starting address
        :type       starting_addr:  int
        :param      coil_qty:       The amount of coils to read
        :type       coil_qty:       int

        :returns:   State of read coils as list
        :rtype:     List[bool]
        """
        modbus_pdu = functions.read_coils(starting_address=starting_addr,
                                          quantity=coil_qty)

        resp_data = self._send_receive(modbus_pdu=modbus_pdu,
                                       slave_addr=slave_addr,
                                       count=True)
        status_pdu = functions.bytes_to_bool(byte_list=resp_data,
                                             bit_qty=coil_qty)

        return status_pdu

    def read_discrete_inputs(self,
                             slave_addr: int,
                             starting_addr: int,
                             input_qty: int) -> List[bool]:
        """
        Read discrete inputs (ISTS).

        :param      slave_addr:     The slave address
        :type       slave_addr:     int
        :param      starting_addr:  The discrete input starting address
        :type       starting_addr:  int
        :param      input_qty:      The amount of discrete inputs to read
        :type       input_qty:      int

        :returns:   State of read discrete inputs as list
        :rtype:     List[bool]
        """
        modbus_pdu = functions.read_discrete_inputs(
            starting_address=starting_addr,
            quantity=input_qty)

        resp_data = self._send_receive(modbus_pdu=modbus_pdu,
                                       slave_addr=slave_addr,
                                       count=True)
        status_pdu = functions.bytes_to_bool(byte_list=resp_data,
                                             bit_qty=input_qty)

        return status_pdu

    def read_holding_registers(self,
                               slave_addr: int,
                               starting_addr: int,
                               register_qty: int,
                               signed: bool = True) -> Tuple[int, ...]:
        """
        Read holding registers (HREGS).

        :param      slave_addr:     The slave address
        :type       slave_addr:     int
        :param      starting_addr:  The holding register starting address
        :type       starting_addr:  int
        :param      register_qty:   The amount of holding registers to read
        :type       register_qty:   int
        :param      signed:         Indicates if signed
        :type       signed:         bool

        :returns:   State of read holding register as tuple
        :rtype:     Tuple[int, ...]
        """
        modbus_pdu = functions.read_holding_registers(
            starting_address=starting_addr,
            quantity=register_qty)

        resp_data = self._send_receive(modbus_pdu=modbus_pdu,
                                       slave_addr=slave_addr,
                                       count=True)
        register_value = functions.to_short(byte_array=resp_data,
                                            signed=signed)

        return register_value

    def read_input_registers(self,
                             slave_addr: int,
                             starting_addr: int,
                             register_qty: int,
                             signed: bool = True) -> Tuple[int, ...]:
        """
        Read input registers (IREGS).

        :param      slave_addr:     The slave address
        :type       slave_addr:     int
        :param      starting_addr:  The input register starting address
        :type       starting_addr:  int
        :param      register_qty:   The amount of input registers to read
        :type       register_qty:   int
        :param      signed:         Indicates if signed
        :type       signed:         bool

        :returns:   State of read input register as tuple
        :rtype:     Tuple[int, ...]
        """
        modbus_pdu = functions.read_input_registers(
            starting_address=starting_addr,
            quantity=register_qty)

        resp_data = self._send_receive(modbus_pdu=modbus_pdu,
                                       slave_addr=slave_addr,
                                       count=True)
        register_value = functions.to_short(byte_array=resp_data,
                                            signed=signed)

        return register_value

    def write_single_coil(self,
                          slave_addr: int,
                          output_address: int,
                          output_value: Union[int, bool]) -> bool:
        """
        Update a single coil.

        :param      slave_addr:      The slave address
        :type       slave_addr:      int
        :param      output_address:  The output address
        :type       output_address:  int
        :param      output_value:    The output value
        :type       output_value:    Union[int, bool]

        :returns:   Result of operation
        :rtype:     bool
        """
        modbus_pdu = functions.write_single_coil(output_address=output_address,
                                                 output_value=output_value)

        resp_data = self._send_receive(modbus_pdu=modbus_pdu,
                                       slave_addr=slave_addr,
                                       count=False)
        operation_status = functions.validate_resp_data(
            data=resp_data,
            function_code=Const.WRITE_SINGLE_COIL,
            address=output_address,
            value=output_value,
            signed=False)

        return operation_status

    def write_single_register(self,
                              slave_addr: int,
                              register_address: int,
                              register_value: int,
                              signed=True) -> bool:
        """
        Update a single register.

        :param      slave_addr:        The slave address
        :type       slave_addr:        int
        :param      register_address:  The register address
        :type       register_address:  int
        :param      register_value:    The register value
        :type       register_value:    int
        :param      signed:            Indicates if signed
        :type       signed:            bool

        :returns:   Result of operation
        :rtype:     bool
        """
        modbus_pdu = functions.write_single_register(register_address,
                                                     register_value,
                                                     signed)

        resp_data = self._send_receive(modbus_pdu=modbus_pdu,
                                       slave_addr=slave_addr,
                                       count=False)
        operation_status = functions.validate_resp_data(
            data=resp_data,
            function_code=Const.WRITE_SINGLE_REGISTER,
            address=register_address,
            value=register_value,
            signed=signed)

        return operation_status

    def write_multiple_coils(self,
                             slave_addr: int,
                             starting_address: int,
                             output_values: List[Union[int, bool]]) -> bool:
        """
        Update multiple coils.

        :param      slave_addr:        The slave address
        :type       slave_addr:        int
        :param      starting_address:  The address of the first coil
        :type       starting_address:  int
        :param      output_values:     The output values
        :type       output_values:     List[Union[int, bool]]

        :returns:   Result of operation
        :rtype:     bool
        """
        modbus_pdu = functions.write_multiple_coils(
            starting_address=starting_address,
            value_list=output_values)

        resp_data = self._send_receive(modbus_pdu=modbus_pdu,
                                       slave_addr=slave_addr,
                                       count=False)
        operation_status = functions.validate_resp_data(
            data=resp_data,
            function_code=Const.WRITE_MULTIPLE_COILS,
            address=starting_address,
            quantity=len(output_values))

        return operation_status

    def write_multiple_registers(self,
                                 slave_addr: int,
                                 starting_address: int,
                                 register_values: List[int],
                                 signed=True) -> bool:
        """
        Update multiple registers.

        :param      slave_addr:        The slave address
        :type       slave_addr:        int
        :param      starting_address:  The starting address
        :type       starting_address:  int
        :param      register_values:   The register values
        :type       register_values:   List[int]
        :param      signed:            Indicates if signed
        :type       signed:            bool

        :returns:   Result of operation
        :rtype:     bool
        """
        modbus_pdu = functions.write_multiple_registers(
            starting_address=starting_address,
            register_values=register_values,
            signed=signed)

        resp_data = self._send_receive(modbus_pdu=modbus_pdu,
                                       slave_addr=slave_addr,
                                       count=False)
        operation_status = functions.validate_resp_data(
            data=resp_data,
            function_code=Const.WRITE_MULTIPLE_REGISTERS,
            address=starting_address,
            quantity=len(register_values),
            signed=signed
        )

        return operation_status

    def send_response(self,
                      slave_addr: int,
                      function_code: int,
                      request_register_addr: int,
                      request_register_qty: int,
                      request_data: list,
                      values: Optional[list] = None,
                      signed: bool = True) -> None:
        """
        Send a response to a client.

        :param      slave_addr:             The slave address
        :type       slave_addr:             int
        :param      function_code:          The function code
        :type       function_code:          int
        :param      request_register_addr:  The request register address
        :type       request_register_addr:  int
        :param      request_register_qty:   The request register qty
        :type       request_register_qty:   int
        :param      request_data:           The request data
        :type       request_data:           list
        :param      values:                 The values
        :type       values:                 Optional[list]
        :param      signed:                 Indicates if signed
        :type       signed:                 bool
        """
        modbus_pdu = functions.response(
            function_code=function_code,
            request_register_addr=request_register_addr,
            request_register_qty=request_register_qty,
            request_data=request_data,
            value_list=values,
            signed=signed
        )
        self._send(modbus_pdu=modbus_pdu, slave_addr=slave_addr)

    def send_exception_response(self,
                                slave_addr: int,
                                function_code: int,
                                exception_code: int) -> None:
        """
        Send an exception response to a client.

        :param      slave_addr:      The slave address
        :type       slave_addr:      int
        :param      function_code:   The function code
        :type       function_code:   int
        :param      exception_code:  The exception code
        :type       exception_code:  int
        """
        modbus_pdu = functions.exception_response(
            function_code=function_code,
            exception_code=exception_code)
        self._send(modbus_pdu=modbus_pdu, slave_addr=slave_addr)

    def get_request(self,
                    unit_addr_list: List[int],
                    timeout: Optional[int] = None) -> Union[Request, None]:
        """
        Check for request within the specified timeout

        :param      unit_addr_list:  The unit address list
        :type       unit_addr_list:  Optional[list]
        :param      timeout:         The timeout
        :type       timeout:         Optional[int]

        :returns:   A request object or None.
        :rtype:     Union[Request, None]
        """
        req = self._uart_read_frame(timeout=timeout)

        if len(req) < 8:
            return None

        if req[0] not in unit_addr_list:
            return None

        req_crc = req[-Const.CRC_LENGTH:]
        req_no_crc = req[:-Const.CRC_LENGTH]
        expected_crc = self._calculate_crc16(req_no_crc)

        if (req_crc[0] != expected_crc[0]) or (req_crc[1] != expected_crc[1]):
            return None

        try:
            request = Request(interface=self, data=req_no_crc)
        except ModbusException as e:
            self.send_exception_response(
                slave_addr=req[0],
                function_code=e.function_code,
                exception_code=e.exception_code)
            return None

        return request
