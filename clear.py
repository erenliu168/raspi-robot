import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
#GPIO.output(31, 1)
#GPIO.output(33, 0)
#GPIO.output(35, 1)
#GPIO.output(37, 0)
#time.sleep(1)
GPIO.cleanup()
