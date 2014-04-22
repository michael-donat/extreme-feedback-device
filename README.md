extreme-feedback-device
=======================

A little project to construct Raspberry Pi based XFD with interface to read Atlassian Bamboo and Jenkins feed. I wrote a blog post on how to construct one [here](http://thornag.github.io/blog/).

Dependencies (apart from python)
--------------------------------

 - pycurl - for bamboo
 - jenkinsapi - for jenkins
 - RPi.GPIO - to control the Pi

Everything should be available via pip

I also recommend running the RPi IPE OS. This will allow you to easily mount the entire filesystem as r/o - somewhat extending the life of your SD card.

Configuration
-------------

You will need to know which pins have been used to wire the relay - the numbers used are the numbers provided by GPIO library, not the chip or pin numbers.

Installation and Running
------------------------

    cd src
    screen python main.py

Screen is probably the easiest way to run the entire process 'in the background'.