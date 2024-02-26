# AYAB Hardware Testing
This is a repository with firmware used for bringup/validation of AYAB hardware. 
Currently the only supported platform is the new AYAB-ESP32.

Start an interactive debug session (add -d to debug serial/slip-encode stream)

```
$ python3 -i ayab_cli.py

INFO:HW CLI:Connected to /dev/ttyACM0 ...

>>> ayab.digitalWrite(board.LED_R, 0)
>>> import tests
>>> tests.tesEOL(ayab)
```
