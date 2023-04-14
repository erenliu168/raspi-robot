import sys
import tty
import termios
import RPi.GPIO as GPIO
import time
pin=[31,33,35,37]
forward=[0,1,1,0]
back=[1,0,0,1]
right=[0,1,0,1]
left=[1,0,1,0]
stop=[1,1,1,1]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
pwm1 = GPIO.PWM(38,80)
pwm2 = GPIO.PWM(40,80)
pwm1.start(80)
pwm2.start(80)
GPIO.output(pin, stop)

def readchar():
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
  return ch
 
def readkey(getchar_fn=None):
  getchar = getchar_fn or readchar
  c1 = getchar()
  if ord(c1) != 0x1b:
    return c1
  c2 = getchar()
  if ord(c2) != 0x5b:
    return c1
  c3 = getchar()
  return chr(0x10 + ord(c3) - 65)
 
while True:
  key=readkey()
  if key=='w':
    GPIO.output(pin, forward)
  if key=='a':
    GPIO.output(pin, left)
  if key=='s':
    GPIO.output(pin, back)
  if key=='d':
    GPIO.output(pin, right)
  if key=='e':
    GPIO.output(pin, stop)
  if key=='q':
    GPIO.cleanup()
    break
  time.sleep(0.5)
  GPIO.output(pin, stop)



