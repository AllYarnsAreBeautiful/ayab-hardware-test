# MCP23017 Register Map (IOCON.BANK = 0, default/POR)
IODIRA   = 0x00
IODIRB   = 0x01
IPOLA    = 0x02
IPOLB    = 0x03
GPINTENA = 0x04
GPINTENB = 0x05
DEFVALA  = 0x06
DEFVALB  = 0x07
INTCONA  = 0x08
INTCONB  = 0x09
IOCONA   = 0x0A
IOCONB   = 0x0B
GPPUA    = 0x0C
GPPUB    = 0x0D
INTFA    = 0x0E
INTFB    = 0x0F
INTCAPA  = 0x10
INTCAPB  = 0x11
GPIOA    = 0x12
GPIOB    = 0x13
OLATA    = 0x14
OLATB    = 0x15

pinMap = [0xF, 0xE, 0xD, 0xC, 0xB, 0xA, 0x9, 0x8,
          0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7]

class Solenoids:
   def __init__(self, api, i2cAddress):
      self._api = api
      self._i2cAddress = i2cAddress
      self.setAllOff()
      self._api.i2cWrite(self._i2cAddress, IODIRA, 0x00)
      self._api.i2cWrite(self._i2cAddress, IODIRB, 0x00)

   def setAllOff(self):
      self._api.i2cWrite(self._i2cAddress, OLATA, 0x00)
      self._api.i2cWrite(self._i2cAddress, OLATB, 0x00)

   def setAllOn(self):
      self._api.i2cWrite(self._i2cAddress, OLATA, 0xff)
      self._api.i2cWrite(self._i2cAddress, OLATB, 0xff)

   def getPort(self, port):
      pin = pinMap[port]
      gpio = GPIOA
      if pin >= 8:
        gpio = GPIOB
        pin -= 8

      return (self._api.i2cRead(self._i2cAddress, gpio) >> pin) & 0x1

   def setPort(self, port, value):
      pin = pinMap[port]
      olat = OLATA
      if pin >= 8:
         olat = OLATB
         pin -= 8

      data = self._api.i2cRead(self._i2cAddress, olat)
      if value != 0:
         data |= (1 << pin)
      else:
         data &= ~(1 << pin)

      self._api.i2cWrite(self._i2cAddress, olat, (data & 0xff))

   def setPorts(self, value):
      data = 0
      for i in range(16):
         if value & (1<<i):
            data += 1 << pinMap[i]
      self._api.i2cWrite(self._i2cAddress, OLATA, (data & 0xff))
      self._api.i2cWrite(self._i2cAddress, OLATB, ((data >> 8) & 0xff))
