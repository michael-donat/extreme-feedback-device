import RPi.GPIO as GPIO;
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

for x in range(0, 60):
	if x % 2 == 0:
		GPIO.output(7, True)
	else:
		GPIO.output(7, False)

	time.sleep(0.4)

GPIO.cleanup()
