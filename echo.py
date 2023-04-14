import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
# 设置超声波传感器的管脚
trigger_pin = 12
echo_pin = 16
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)
# 发射超声波，并计算回响时间
GPIO.output(trigger_pin, GPIO.LOW)
time.sleep(0.2)
GPIO.output(trigger_pin, GPIO.HIGH)
time.sleep(0.00002)
GPIO.output(trigger_pin, GPIO.LOW)
while GPIO.input(echo_pin) == GPIO.LOW:
    start_time = time.time()
while GPIO.input(echo_pin) == GPIO.HIGH:
    end_time = time.time()
# 计算距离并输出
duration = end_time - start_time
print(duration)
distance = round(duration * 17150, 2)
if duration>499:
    print("error dis: ", duration, "cm")
else:
    print("Distance: ", distance, "cm")
GPIO.cleanup()
