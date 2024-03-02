import argparse
import logging
import sys

import ayab.board as board
from ayab.api import API
from ayab.comm import AyabCommunication
from ayab.solenoids import Solenoids

# Default parameters
SERIAL_PORT = '/dev/ttyACM0'

# -------------------------------------------------------------------------
# Parse command line
# -------------------------------------------------------------------------

parser = argparse.ArgumentParser(description="Ayab HW CLI.")
parser.add_argument("-s", type=str, help=f"Serial interface ({SERIAL_PORT})", default=SERIAL_PORT)
parser.add_argument("-d",           help="ENable debug loglevel", action="store_true")

args = parser.parse_args()

# -------------------------------------------------------------------------
# Setup
# -------------------------------------------------------------------------

# Setup logger
loglevel = logging.DEBUG if args.d else logging.INFO
logging.basicConfig(stream=sys.stdout, level=loglevel)

logger = logging.getLogger("HW CLI")

# Open serial interface (triggers an Arduino reset)
comm=AyabCommunication(loglevel=loglevel)
try:
  comm.open_serial(args.s)
  logger.info(f"Connected to {args.s} ...\n")
except:
  logger.info('ERROR: Unable to open serial interface\n')
  sys.exit(1)

api = API(comm)
solenoids = Solenoids(api, board.MCP23017_I2CADDR)

# api.digitalRead() 
# api.i2cWrite(board.MCP23017_I2CADDR,0x14,0xa5) # OLATA(0x14)=0xa5
# api.i2cRead(board.MCP23017_I2CADDR,0x12)       # Read GPIOA
#
# solenoids.setAllOff()
# solenoids.setPorts(0xa55a)
# solenoids.setPort(0, 1)
# solenoids.getPort(0)
# solenoids.setAllOn()
#
# import tests
# tests.testEOL(api)

# -------------------------------------------------------------------------
# Main loop
# -------------------------------------------------------------------------
