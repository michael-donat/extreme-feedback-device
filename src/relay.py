import RPi.GPIO as GPIO;

class Relay:
    __config=None
    def __init__(self, config):
        self.__config=config
        GPIO.setmode(GPIO.BOARD);
        GPIO.setwarnings(False)
        GPIO.setup(self.__config.getint('Relay', 'powerPin'), GPIO.OUT)
        GPIO.setup(self.__config.getint('Relay', 'lightPin'), GPIO.OUT)
        pass

    def powerOn(self):
        GPIO.output(self.__config.getint('Relay', 'powerPin'), self.__config.getboolean('Relay', 'powerOnValue'))

    def powerOff(self):
        GPIO.output(self.__config.getint('Relay', 'powerPin'), not self.__config.getboolean('Relay', 'powerOnValue'))

    def passLight(self):
        GPIO.output(self.__config.getint('Relay', 'lightPin'), self.__config.getboolean('Relay', 'passValue'))

    def failLight(self):
        GPIO.output(self.__config.getint('Relay', 'lightPin'), not self.__config.getboolean('Relay', 'passValue'))

    def cleanup(self):
        GPIO.cleanup()
