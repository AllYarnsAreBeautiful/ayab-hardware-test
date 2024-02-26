import board

def testEOL(ayab):
  print("Testing the end of line sensors.\n")
  rightNorth = ayab.digitalRead(board.EOL_R_N);
  rightSouth = ayab.digitalRead(board.EOL_R_S);
  leftNorth  = ayab.digitalRead(board.EOL_L_N);
  leftSouth  = ayab.digitalRead(board.EOL_L_S);

  print(f"EOL L North: {leftNorth}, " South: {leftSouth}, EOL R North: {rightNorth}, South: {rightSouth}\n")
