import RPi.GPIO as GPIO
import time
pin=[31,33,35,37]
forward=[0,1,1,0]
back=[1,0,0,1]
left=[0,1,0,0]
right=[0,0,1,0]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.output(pin, forward)
time.sleep(1)
#time.sleep(5)
#GPIO.output(pin, right)
#time.sleep(4)
#GPIO.output(pin, forward)
#time.sleep(5)
#GPIO.output(pin, right)
#time.sleep(4)
#GPIO.output(pin, forward)
#time.sleep(5)
#GPIO.cleanup()
