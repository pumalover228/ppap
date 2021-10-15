import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt


dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds= [21, 20, 16, 12, 7, 8, 25,24]
bits = len(dac)
levels = 2**bits
maxU = 3.3
troyka = 17
comp = 4

dannie=[]
time0=time.time()

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


def dec2bin (value):
    return [int(bin) for bin in bin(value)[2:].zfill(bits)]

def bin2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    GPIO.output(leds, signal)
    return signal

def adc():
    global value
    global voltage
    for value in range(256):
        signal = bin2dac(value)
        voltage = value / levels * maxU
        time.sleep(0.003)
        compValue = GPIO.input(comp)
        if compValue == 0:
            print (" Digital value: {:^3} -> {}, Analog value: {:.2f}".format(value, signal, voltage))
            dannie.append(voltage)
            break



try:
    while True:
        adc()
        if value>250:
            break

finally:
    GPIO.cleanup(dac)
    GPIO.cleanup(leds)

plt.plot(dannie)
plt.show()


dannie_str=[str(x) for x in dannie]
with open('itog.txt','w') as f:
    f.write('\n'.join(dannie_str))