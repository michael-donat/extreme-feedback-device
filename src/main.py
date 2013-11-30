__author__ = 'thornag'

from controller import Controller
from ConfigParser import ConfigParser
from relay import Relay
import time

import feed

cnf = ConfigParser()
cnf.read('../config.ini')

ctrl = Controller(cnf, Relay(cnf), feed.Bamboo(cnf))
bStatus = ctrl.processCircuitPower()

if bStatus:

    bStatus = ctrl.processLampColor()

    if bStatus:
        print time.strftime('%H:%M:%S Circuit...   ON, Color...     BLUE')
    else:
        print time.strftime('%H:%M:%S Circuit...   ON, Color...     RED')

else:
     print time.strftime('%H:%M:%S Circuit...   OFF')

