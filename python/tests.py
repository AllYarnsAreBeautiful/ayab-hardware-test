import ayab.board as board

def testEOL(api):
  print("Testing the end of line sensors.\n")
  rightNorth = api.digitalRead(board.EOL_R_N)
  rightSouth = api.digitalRead(board.EOL_R_S)
  leftNorth  = api.digitalRead(board.EOL_L_N)
  leftSouth  = api.digitalRead(board.EOL_L_S)

  print(f"EOL L North: {leftNorth}, South: {leftSouth}, EOL R North: {rightNorth}, South: {rightSouth}\n")
