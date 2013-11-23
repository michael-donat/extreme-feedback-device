__author__ = 'thornag'

import unittest, ConfigParser

from controller import Controller


class TestController(unittest.TestCase):
    def test_isWithinTime(self):

        config = ConfigParser.ConfigParser()
        config.add_section('Time')
        config.set('Time', 'onAt', '08:00')
        config.set('Time', 'offAt', '20:00')

        controller = Controller(config)

        self.assertFalse(controller.shouldBeOnAt('21:00'))
        self.assertFalse(controller.shouldBeOnAt('20:01'))
        self.assertTrue(controller.shouldBeOnAt('08:00'))
        self.assertTrue(controller.shouldBeOnAt('20:00'))


if __name__ == '__main__':
    unittest.main()
