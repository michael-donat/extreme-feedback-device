__author__ = 'thornag'

from controller import Controller
from ConfigParser import ConfigParser
from relay import Relay
import feed

cnf = ConfigParser()
cnf.read('../config.ini')

ctrl = Controller(cnf, Relay(cnf), feed.Bamboo(cnf))
bStatus = ctrl.processCircuitPower()

if bStatus:
    print 'Circuit...   ON'

    bStatus = ctrl.processLampColor()

    if bStatus:
        print 'Color...     BLUE'
    else:
        print 'Color...     RED'

else:
    print 'Circuit...   OFF'

