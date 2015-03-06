# A less ugly hack so that we don't have to install stuff using
# more horrible hacks like virtualenv.
# Come on Guido, even node.js does modules better!
import sys
import os
MY_DIR = os.path.dirname(os.path.abspath(__file__))
FAKE_SITE = os.path.join(MY_DIR, 'fake-site')
RPYC_SERVER = os.path.join(FAKE_SITE, 'rpyc_classic.py') 
sys.path.append(FAKE_SITE)

from rpyc.utils import factory
from rpyc import SlaveService

PYTHON_EXECUTABLE='/usr/bin/python'

def pyslave(python=None):
    if python is None:
        python = PYTHON_EXECUTABLE
    slave = factory.connect_subproc([python, "-u", RPYC_SERVER, "-q", "-m", "stdio"],
            SlaveService)
    
    # Connect standard streams so we get some output too
    slave.modules.sys.stdout = sys.stdout
    slave.modules.sys.stderr = sys.stderr

    # PyPy won't accept this as module without these
    slave.__nonzero__ = lambda: True
    slave.__path__ = lambda: None

    return slave

