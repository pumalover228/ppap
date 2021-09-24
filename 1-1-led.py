'''import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
for i in range(5):
    GPIO.output(14,1)
    time.sleep(0.5)
    GPIO.output(14,0)
    time.sleep(0.5)'''

'''import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15, GPIO.IN)
while True:
    print(GPIO.input(14))'''


import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)

GPIO.setup(14,GPIO.OUT)
GPIO.setup(15, GPIO.IN)
value=GPIO.input(15)
state=0
while True:
    if (value==0 and GPIO.input(15)==1):
        state=not state
        GPIO.output(14,state)
        time.sleep(1)
    value=GPIO.input(15)