import RPi.GPIO as GPIO
import time
dac=[26, 19, 13, 6, 5, 11, 9, 10]
bits=len(dac)
levels=2**bits
maxvoltage=3.3
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
def f(n):
    return [int(bit) for bit in bin(n)[2::].zfill(bits)]
def u(n):
    signal=f(n)
    GPIO.output(dac,signal)
    return signal
'''
try:
    while True:
        b=input()
        if b.isdigit():
            c=int(b)
            if c>=levels:
                continue
            signal = u(c)
            voltage=c*maxvoltage/levels
        elif b=='q':
            break
        else:
            continue
except:
    pass
else:
    pass
finally:
    GPIO.output(dac,GPIO.LOW)
    GPIO.cleanup'''

p=int(input())
for j in range(2*p):
    if not j%2:
        for i in range(256):
            t=u(i)
            time.sleep(0.001)
    if j%2:
        for i in range(255,0,-1):
            t=u(i)
            time.sleep(0.001)
    
'''
except:
    pass
else:
    pass
finally:
    GPIO.output(dac,GPIO.LOW)
    GPIO.cleanup'''
