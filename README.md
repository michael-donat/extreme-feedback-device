extreme-feednack-device
=======================

A little project to construct Raspberry Pi based XFD with interface to read Atlassian Bamboo feed.

Shopping list
------------

Raspberry Pi
SainsSmart 2 channel relay
Female-female jumper leads
Housing box
2 LED coloured bulbs
Extension lead
Wire joining strip
Some spare wires and plugs


How to
------------

Idea is to run the controlling software every 2-5 minutes with cron. There is a configuration file that
specifies when the system is in 'on' state - this has been added to completely disable power put on the
circuit when there is no people in the office (say between 8pm an 8am).

The first relay (r1) switch is responsible for cosing the cirrcuit from the mains, thus providing power. Controlling software
will compare current time with conigured time and switch r1 accordingly.

The second relay is responsible for swapping light colour. Depending on whether there are broken build in the feed the red or blue/greem light will be on.

Above is illustrated by wiring and sequence diagrams below:

(https://raw2.github.com/thornag/extreme-feedback-device/master/resources/relay_algorithm.png)

(https://raw2.github.com/thornag/extreme-feedback-device/master/resources/simple_wiring.png)



Software dependencies (apart from python)
------------

    pycurl
    RPi.GPIO

Both can be installed with either easy_install, pip or via os package manager (apt-get).


Configuration
-------------

Running
-------------
