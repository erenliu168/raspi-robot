import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

sensor_pin_right = 18
sensor_pin_left = 7
GPIO.setup(sensor_pin_right, GPIO.IN)
GPIO.setup(sensor_pin_left, GPIO.IN)

while True:
    if not GPIO.input(sensor_pin_right):
        print("Right: Object detected")
    else:
        print("Right: No object detected")
    if not GPIO.input(sensor_pin_left):
        print("Left: Object detected")
    else:
        print("Left: No object detected")
    
    time.sleep(1)
