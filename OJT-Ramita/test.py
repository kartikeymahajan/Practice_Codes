import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv
data = []
with open('ecg.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.extend(row)

datalen = 704718
fs = 10  # Sampling frequency (samples per second)
t = np.arange(0, 5000,) # Time vector from 0 to 10 seconds
ecg_data = 0.5 * np.sin(2 * np.pi * 1 * t) # Simulated ECG data

new_ecg_data = [eval(i) for i in data]

fig, ax = plt.subplots()
line, = ax.plot([], [])

def init():
    ax.set_xlim(0, 5000)
    ax.set_ylim(-5, 5)
    return line,

def animate(i):
    x = t[:i]
    y = new_ecg_data[:i]
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(t), interval=10, blit=True)

plt.show()