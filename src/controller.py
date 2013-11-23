import datetime

class Controller:
    __config=None
    def __init__(self, config):
        self.__config = config


    def shouldBeOnAt(self, timeHHMM):
        hours, minutes = timeHHMM.split(':')
        now = datetime.datetime.now()
        now = now.replace(hour=int(hours), minute=int(minutes))

        hours, minutes = self.__config.get('Time', 'onAt').split(':')
        onAt = now.replace(hour=int(hours), minute=int(minutes))

        hours, minutes = self.__config.get('Time', 'offAt').split(':')
        offAt = now.replace(hour=int(hours), minute=int(minutes))

        return now >= onAt and now <= offAt



