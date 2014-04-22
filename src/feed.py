#import pycurl
import sys
import getopt
import StringIO
import xml.etree.ElementTree as ET

class Bamboo:
    __feed=None
    __user=None
    __pass=None
    __failures=None
    def __init__(self, config):
        self.__feed = config.get('Feed', 'url')
        self.__user = config.get('Feed', 'user')
        self.__pass = config.get('Feed', 'password')

    def process(self):
        b = StringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, self.__feed)
        c.setopt(pycurl.VERBOSE, 0)
        c.setopt(pycurl.WRITEFUNCTION, b.write)
        c.setopt(pycurl.USERPWD, '%s:%s' % (self.__user, self.__pass))
        c.perform()

        xml = b.getvalue()

        xml = ET.fromstring(xml)

        self.__failures = False

        for node in xml.iter('result'):
            plan = node.find('plan')
            if plan.attrib['enabled'] == 'false':
                continue
            state = node.attrib['state']
            if state == 'Failed':
                self.__failures = True
                break

    def hasFailures(self):
        return self.__failures

class Jenkins:
    __requester=None
    __jenkins=None
    __jobName=None
    __failures=None
    def __init__(self, config):
        from jenkinsapi.jenkins import Jenkins
        from jenkinsapi.utils.requester import Requester
        self.__requester = Requester(config.get('Feed', 'user'), config.get('Feed', 'password'), False)
        self.__jenkins = Jenkins(config.get('Feed', 'url'), config.get('Feed', 'user'), config.get('Feed', 'password'), self.__requester)
        self.__jobName = config.get('Feed', 'job')

    def process(self):
        job =self.__jenkins[self.__jobName]
        lb = job.get_last_build()
        self.__failures = lb.get_status() == 'FAILURE'

    def hasFailures(self):
        return self.__failures
