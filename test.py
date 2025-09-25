import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
try:
	GPIO.output(4,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(4,GPIO.LOW)
finally:
	GPIO.cleanup()
