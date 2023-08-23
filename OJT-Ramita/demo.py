import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

with open('ecg.csv', 'r') as file:
    csv_reader = csv.reader(file)
    data = next(csv_reader)

fs = 100 # Sampling frequency (samples per second)
t = np.arange(0, 10, 1/fs) # Time vector from 0 to 10 seconds
ecg_data = 0.5 * np.sin(2 * np.pi * 1 * t)
# new_ecg = np.sin(data)
# print(new_ecg)
# print(type(np.sin(2 * np.pi * 1 * t)))
# print(ecg_data)
ll = np.array(data)
print(ll)
print(type(ll)) 