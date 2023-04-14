import RPi.GPIO as GPIO
import time

# 定义GPIO引脚编号
motor_pin=[31,33,35,37]
trigger_pin = 12
echo_pin = 16
sensor_pin_right = 18
sensor_pin_left = 7

# 定义占空比等级
pwm_level=[0,20,40,60,80,100]

# action
forward=[0,1,1,0]
back=[1,0,0,1]
tank_right=[0,1,0,1]
right=[0,1,0,0]
tank_left=[1,0,1,0]
left=[0,0,1,0]
stop=[1,1,1,1]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
# set ray gpio
GPIO.setup(sensor_pin_right, GPIO.IN)
GPIO.setup(sensor_pin_left, GPIO.IN)
# 设置超声波传感器的管脚
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

pwm1 = GPIO.PWM(38, 200)
pwm2 = GPIO.PWM(40, 200)
pwm1.start(pwm_level[0])
pwm2.start(pwm_level[0])

def set_speed(m,n):
    pwm1.ChangeDutyCycle(pwm_level[m])
    pwm2.ChangeDutyCycle(pwm_level[n])

def get_dis():
    # 发射超声波，并计算回响时间
    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, GPIO.LOW)
    while GPIO.input(echo_pin) == GPIO.LOW:
        start_time = time.time()
    while GPIO.input(echo_pin) == GPIO.HIGH:
        end_time = time.time()
    # 计算距离并输出
    duration = end_time - start_time
    distance = round(duration * 17150, 2)
    if distance > 499:
        print("Error dis: ", distance, "cm")
        distance = 10
    else:
        print("Distance: ", distance, "cm")
    return distance
def adjust(f,r,l):
    if f:
        if r and not l:
            GPIO.output(motor_pin,tank_left)
            set_speed(4,4)
        elif not r and l:
            GPIO.output(motor_pin,tank_right)
            set_speed(4,4)
        elif not r and not l:
            GPIO.output(motor_pin, tank_right)
            set_speed(4,4)
        else:
            GPIO.output(motor_pin, stop)
            set_speed(5,5)
    else:
        if r and not l:
            GPIO.output(motor_pin,forward)
            set_speed(1,5)
        elif not r and l:
            GPIO.output(motor_pin,forward)
            set_speed(5,1)
        elif not r and not l:
            GPIO.output(motor_pin, forward)
            set_speed(3,3)
        else:
            GPIO.output(motor_pin, stop)
            set_speed(5,5)
try: 
  while True:
      f = False
      r = False
      l = False
      if get_dis()<20:
          print("Too close in front.")
          GPIO.output(motor_pin, stop)
          f = True
      if not GPIO.input(sensor_pin_right):
          print("Right: Object detected")
          GPIO.output(motor_pin, stop)
          r = True
      if not GPIO.input(sensor_pin_left):
          print("Left: Object detected")
          GPIO.output(motor_pin, stop)
          l = True
      adjust(f,r,l)
except Exception as e:
    print(str(e))
finally:
    GPIO.cleanup()
