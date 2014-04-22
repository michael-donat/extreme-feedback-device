__author__ = 'thornag'

import sys, signal, time, ConfigParser
import feed, relay, controller

cnf = ConfigParser.ConfigParser()
cnf.read('../config.ini')

ctrl = controller.Controller(cnf, relay.Relay(cnf), feed.Jenkins (cnf))
bCircuitStatus = ctrl.processCircuitPower()

for sig in [signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGQUIT]:
    signal.signal(sig, ctrl.cleanup)
try:
    while(True):
        if bCircuitStatus:

            bStatus = ctrl.processLampColor()

            if bStatus:
                print time.strftime('%H:%M:%S Circuit...   ON, Color...     BLUE')
            else:
                print time.strftime('%H:%M:%S Circuit...   ON, Color...     RED')

        else:
             print time.strftime('%H:%M:%S Circuit...   OFF')

        time.sleep(cnf.getint('Time', 'frequency'))
except (KeyboardInterrupt, SystemExit):
    ctrl.cleanup()
    sys.exit(0)
