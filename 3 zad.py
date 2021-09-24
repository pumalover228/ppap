import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p=GPIO.PWM(12,1000)
def change(dc):
    p.start(dc)

while True:
    dc=int(input())
    change(dc)