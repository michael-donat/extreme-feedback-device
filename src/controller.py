import datetime, time

class Controller:
    __config=None
    __isOn=None
    __relay=None
    __feed=None
    def __init__(self, config, relay, feed):
        self.__config = config
        self.__relay = relay
        self.__feed = feed

    def processCircuitPower(self):
        if self.shouldBeOnAt(time.strftime('%H:%M')):
            self.__isOn=True
            self.__relay.powerOn()
        else:
            self.__isOn=False
            self.__relay.powerOff()

        return self.__isOn

    def processLampColor(self):
        if not self.__isOn:
            return

        self.__feed.process()
        if self.__feed.hasFailures():
            self.__relay.failLight()
        else:
            self.__relay.passLight()

        return not self.__feed.hasFailures()


    def shouldBeOnAt(self, timeHHMM):
        hours, minutes = timeHHMM.split(':')
        now = datetime.datetime.now()
        now = now.replace(hour=int(hours), minute=int(minutes))

        hours, minutes = self.__config.get('Time', 'onAt').split(':')
        onAt = now.replace(hour=int(hours), minute=int(minutes))

        hours, minutes = self.__config.get('Time', 'offAt').split(':')
        offAt = now.replace(hour=int(hours), minute=int(minutes))

        return now >= onAt and now <= offAt



