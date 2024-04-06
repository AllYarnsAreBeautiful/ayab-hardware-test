import argparse
import logging
import sys

import board
from ayab_api import API
from ayab_communication import AyabCommunication

# Default parameters
SERIAL_PORT = '/dev/ttyACM0'

# -------------------------------------------------------------------------
# Parse command line
# -------------------------------------------------------------------------

parser = argparse.ArgumentParser(description="Ayab HW CLI.")
parser.add_argument("-p", "--port", type=str, help=f"Serial port (default: {SERIAL_PORT})", default=SERIAL_PORT)
parser.add_argument("-d", "--debug", help="Enable debug log level", action="store_true")

args = parser.parse_args()

# -------------------------------------------------------------------------
# Setup
# -------------------------------------------------------------------------

# Setup logger
loglevel = logging.DEBUG if args.debug else logging.INFO
logging.basicConfig(stream=sys.stdout, level=loglevel)

logger = logging.getLogger("HW CLI")

# Open serial interface (triggers an Arduino reset)
comm=AyabCommunication(loglevel=loglevel)
try:
  comm.open_serial(args.p)
  logger.info(f"Connected to {args.p} ...\n")
except:
  logger.info('ERROR: Unable to open serial interface\n')
  sys.exit(1)

ayab = API(comm)

# -------------------------------------------------------------------------
# Main loop
# -------------------------------------------------------------------------
