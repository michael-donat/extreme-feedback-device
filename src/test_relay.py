import unittest
from relay import Relay

class TestRelay(unittest.TestCase):

    def testControllingDevice(self):
        relay = Relay(None)
        device = relay.device(idVendor=0x16C0,idProduct=0x05DF)
        interface = relay.interface(device)
        interface.write(0b0000001)
        pass

if __name__ == '__main__':
    unittest.main()