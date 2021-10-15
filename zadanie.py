import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt #импорт библиотек


dac = [26, 19, 13, 6, 5, 11, 9, 10] #светодиоды dac
leds= [21, 20, 16, 12, 7, 8, 25,24] #светодиоды leds
bits = len(dac) #количество битов (8 бит - кодировка 256 позиций)
levels = 2**bits
maxU = 3.3 #максимальное напряжение, выдаваемое малинкой
troyka = 17
comp = 4

dannie=[] #массив с данными, куда будут сохраняться измерения
time0=time.time()

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN) #установка dac и leds на выход, подача напряжения на тройку


def dec2bin (value):
    return [int(bin) for bin in bin(value)[2:].zfill(bits)] #функция перевода из 10 в 2

def bin2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    GPIO.output(leds, signal)
    return signal #функция перевода из 2 в 10

def adc(): #основная функция, в которой происходит измерение напряжения и вывод значений
    global value
    global voltage
    for value in range(256):
        signal = bin2dac(value)
        voltage = value / levels * maxU
        time.sleep(0.003)
        compValue = GPIO.input(comp)
        if compValue == 0:
            print (" Digital value: {:^3} -> {}, Analog value: {:.2f}".format(value, signal, voltage))
            dannie.append(voltage) #добавляем измерение напряжения в список данных
            break 



try:
    while True:
        adc()
        if value>250:
            break #при том условии что конденсатор зарядится до почти максимального значения, нужно произвести выход из цикла

finally: #очистка светодиодов
    GPIO.cleanup(dac)
    GPIO.cleanup(leds)

plt.plot(dannie)
plt.show() #делаем график


dannie_str=[str(x) for x in dannie] #переводим данные из массива в строки, чтоб их можно было вписать в файл
with open('itog.txt','w') as f:
    f.write('\n'.join(dannie_str)) #вписываем данные в файл