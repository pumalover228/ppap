import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.ticker as ticker
import numpy as np
from textwrap import wrap


k = 11.147491616392957 # сюда впишите k, полученный в калибровке

with open('fitness.txt', 'r') as fitness:
    tempfitness = fitness.read().split("\n")
    tempfitness_x = []
    tempfitness_y = []
    time = []
    time_time = []
    count = []
    for i in range(10, len(tempfitness), 1):
        tempfitness_y.append(int(tempfitness[i]) / k)
    time_time = tempfitness[3].split(" ")
    time = time_time[4].split(".")
    count = tempfitness[7].split(" ")
    tempfitness_x = np.linspace(0, int(time[0]), int(count[4]))


fig, ax = plt.subplots(figsize=(16, 10), dpi=200)
title = 'Blood pressure after exercises'
ax.set_title("\n".join(wrap(title, 100)))
print(len(tempfitness_x), len(tempfitness_y))
ax.plot(tempfitness_x, tempfitness_y, color='r', linewidth=0.3)
plt.axis([0, int(time[0]) + 5, 30, 170])
plt.ylabel('Pressure [mm]', fontsize=7)
plt.xlabel('Time [s]', fontsize=7)
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax.tick_params(which='major', length=5, labelsize=5)
ax.tick_params(which='minor', length=3)
ax.grid(which='major', color='black', linewidth=0.2)
ax.minorticks_on()
ax.grid(which='minor', color='gray', linestyle=':', linewidth=0.5)
graph = mlines.Line2D([], [], color='r', markersize=30, label='Давление .../... мм рт.ст.') # Вместо ... данные из графика
plt.legend(handles=[graph])

plt.show()
fig.savefig("finalPressure-fitness.png")
