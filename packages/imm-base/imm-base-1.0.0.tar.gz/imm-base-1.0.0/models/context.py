import sys
from pathlib import Path


# Get project's home directory,
BASEDIR = Path(__file__).parents[2]
DATADIR = BASEDIR / "data"

# Insert the BASEDIR to system path
# sys.path.insert(0, BASEDIR)
