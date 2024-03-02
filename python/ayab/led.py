class Led:
   def __init__(self, api, pin):
      self._api = api
      self._pin = pin
      
   def on(self):
      self._api.digitalWrite(self._pin, 1)

   def off(self):
      self._api.digitalWrite(self._pin, 0)
