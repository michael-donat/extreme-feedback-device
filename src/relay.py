import RPi.GPIO as GPIO;

class Relay:
    __config=None
    def __init__(self, config):
        self.__config=config
        GPIO.setmode(GPIO.BOARD);
        GPIO.setup(self.__config.get('Relay', 'powerPin'), GPIO.OUT)
        GPIO.setup(self.__config.get('Relay', 'lightPin'), GPIO.OUT)
        pass

    def powerOn(self):
        GPIO.output(self.__config.get('Relay', 'powerPin'), self.__config.get('Relay', 'powerOnValue'))

    def powerOff(self):
        GPIO.output(self.__config.get('Relay', 'powerPin'), not self.__config.get('Relay', 'powerOnValue'))

    def passLight(self):
        GPIO.output(self.__config.get('Relay', 'lightPin'), self.__config.get('Relay', 'passValue'))

    def failLight(self):
        GPIO.output(self.__config.get('Relay', 'lightPin'), not self.__config.get('Relay', 'passValue'))
