__author__ = 'thornag'

from controller import Controller
from ConfigParser import ConfigParser
from relay import Relay
from feed import Feed

cnf = ConfigParser()
cnf.read('../config.ini')

ctrl = Controller(cnf, Relay(cnf), Feed(cnf))
ctrl.processCircuitPower()
ctrl.processLampColor()
