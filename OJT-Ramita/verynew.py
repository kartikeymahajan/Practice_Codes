import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
sampling_rate = 1000 # Samples per second (Hz)
duration = 1000       # Duration of the ECG signal in seconds

# Time axis
t = np.linspace(0, duration, duration * sampling_rate)
new_t = [0.00, 0.08, 0.12, 0.16, 0.20, 0.24, 0.28, 0.32, 0.40, 0.48, 0.52]

time_increase_pattern = [1, 1, 6, 2, 1]
tip_increased_by = [0.00, 0.08, 0.04, 0.08, 0.04]

for i in range(1, 10):
    for tip, tip_value in zip(time_increase_pattern, tip_increased_by):
        for j in range(tip):
            new_t.append(round(new_t[-1] + tip_value, 2))
                    

# Simulate components of the ECG waveform
p_wave = 0.1 * np.sin(2 * np.pi * 1 * t)  # P-wave at around 1 Hz
qrs_complex = 0.6 * np.sin(2 * np.pi * 4 * t) # QRS complex at around 4 Hz
t_wave = 0.2 * np.sin(2 * np.pi * 0.5 * t)  # T-wave at around 0.5 Hz

# Combine components to create the ECG signal
ecg_signal = p_wave + qrs_complex + t_wave
new_ecg_signal = [0, 0.1, 0.2, 0.1, 0.1, 1.0, -0.4, 0.0, 0.1, 0.0, 0,
                  0, 0.1, 0.2, 0.1, 0.1, 1.0, -0.4, 0.0, 0.1, 0.0, 0,
                  0, 0.1, 0.2, 0.1, 0.1, 1.0, -0.4, 0.0, 0.1, 0.0, 0,
                  0, 0.1, 0.2, 0.1, 0.1, 1.0, -0.4, 0.0, 0.1, 0.0, 0,
                  0, 0.1, 0.2, 0.1, 0.1, 1.0, -0.4, 0.0, 0.1, 0.0, 0,
                  0, 0.1, 0.2, 0.1, 0.1, 1.0, -0.4, 0.0, 0.1, 0.0, 0,
                  0, 0.1, 0.2, 0.1, 0.1, 1.0, -0.4, 0.0, 0.1, 0.0, 0,
                  0, 0.1, 0.2, 0.1, 0.1, 1.0, -0.4, 0.0, 0.1, 0.0, 0,
                  0, 0.1, 0.2, 0.1, 0.1, 1.0, -0.4, 0.0, 0.1, 0.0, 0,
                  0, 0.1, 0.2, 0.1, 0.1, 1.0, -0.4, 0.0, 0.1, 0.0, 0,
                  ]



# Add some noise to the signal
noise = 0.1 * np.random.randn(len(t))
new_noise = 0.1 * np.random.randn(len(new_t))

ecg_signal_with_noise = ecg_signal + noise
new_ecg_signal_with_noise = new_ecg_signal + new_noise


# Plot the simulated ECG signal
plt.figure(figsize=(10, 4))
plt.plot(new_t, new_ecg_signal)
plt.title("Simulated ECG Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()