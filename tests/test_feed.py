__author__ = 'thornag'

import unittest, ConfigParser

import sys

sys.path.append("./../src")

from feed import Jenkins, Bamboo

from ConfigParser import ConfigParser

cnf = ConfigParser()
cnf.read('../config.ini')

class TestFeed(unittest.TestCase):
    def test_checkingJenkinsStatus(self):

        feedJenkins = Jenkins(cnf)
        feedJenkins.process()
        result = feedJenkins.hasFailures()

        pass


if __name__ == '__main__':
    unittest.main()
