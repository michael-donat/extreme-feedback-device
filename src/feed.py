import pycurl
import sys
import getopt

optlist, args = getopt.getopt(sys.argv[1:], 'pu')

user = password = None;

for o, a in optlist:
    if o == "-p":
        password = a;
    elif o == "-u":
        user = a

def getFeedData():
	c = pycurl.Curl()
	c.setopt(pycurl.URL, 'https://monitechnologies.atlassian.net/builds/rss/createAllBuildsRssFeed.action?feedType=rssAll&os_authType=basic')
	c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
	c.setopt(pycurl.VERBOSE, 0)
	c.setopt(pycurl.USERPWD, '%s:%s' % user, password)
	c.perform()


getFeedData()

