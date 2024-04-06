import board
import time

def testEOL(ayab):
  print("Testing the end of line sensors.\n")

  rightNorth = ayab.digitalRead(board.EOL_R_N)
  rightSouth = ayab.digitalRead(board.EOL_R_S)
  leftNorth  = ayab.digitalRead(board.EOL_L_N)
  leftSouth  = ayab.digitalRead(board.EOL_L_S)

  print(f"EOL L North: {leftNorth}, South: {leftSouth}, EOL R North: {rightNorth}, South: {rightSouth}\n")

def testLEDs(ayab):
  print("Blinking LEDs...\n")

  for(i in range(5)):
    ayab.digitalWrite(ayab.LED_R, 1)
    ayab.digitalWrite(ayab.LED_Y, 1)
    ayab.digitalWrite(ayab.LED_G, 1) 
    time.sleep(0.5)

    ayab.digitalWrite(ayab.LED_R, 0)
    ayab.digitalWrite(ayab.LED_Y, 0)
    ayab.digitalWrite(ayab.LED_G, 0)
    time.sleep(0.5)
    
def testEncoder(ayab):
  print("Checking encoder state.\n")
  encA = ayab.digitalRead(ENCODER_A)
  encB = ayab.digitalRead(ENCODER_B)
  encBP = ayab.digitalRead(ENCODER_BELTPHASE)

  print(f"A: {encA}, B: {encB}, Belt Phase: {encBP}\n")

def testSolenoids(ayab):

def testBeeper(ayab):
  print("Testing beeper.\n")

  ayab.buzzerState(1)
  time.sleep(2)
  ayab.buzzerState(0)
  
  print("Did you hear the buzzer?")

def testUserButton(ayab):
  print("Testing user button.\n")

  btn = ayab.digitalRead(ayab.USER_BUTTON)

  print(f"User button state is {btn}")
