import struct

# API Command definition
CMD_DIGITAL_WRITE   = 0x01
CMD_DIGITAL_READ    = 0x02
CMD_I2C_WRITE       = 0x03
CMD_I2C_READ        = 0x04
CMD_SET_STATE       = 0x05

# -------------------------------------------------------------------------
# API Methods
# -------------------------------------------------------------------------
class API:

    def __init__(self, ayab):
        self._ayab = ayab

    def digitalWrite(self, gpio, value):
        self._ayab.send_msg(CMD_DIGITAL_WRITE, bytes(struct.pack("<BB", gpio, value)))

    def digitalRead(self, gpio):
        self._ayab.send_msg(CMD_DIGITAL_READ, bytes((gpio,)))
        # time.sleep(10e-3); # Required ?
        msg = self._ayab.get_msg()
        return msg[1]

    def i2cWrite(self, address, register, value):
        self._ayab.send_msg(CMD_I2C_WRITE, bytes(struct.pack("<BBB", address, register, value)))

    def i2cRead(self, address, register):
        self._ayab.send_msg(CMD_I2C_READ, bytes(struct.pack("<BB", address, register)))
        # time.sleep(10e-3); # Required ?
        msg = self._ayab.get_msg()
        return msg[1]

    def beep(self, duration):
        self._ayab.send_msg(CMD_BEEP, bytes(duration))
