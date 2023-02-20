import numpy as np

# Set the sampling frequency and number of samples
fs = 4000  # Hz
n_samples = 20000



# Create a time vector
time = np.linspace(0, n_samples/fs, n_samples)

# Create synthetic EEG data
# Here we'll create two signals, one with a sine wave and the other with a cosine wave
signal1 = np.sin(2*np.pi*10*time) # 10 Hz sine wave
signal2 = np.cos(2*np.pi*15*time) # 15 Hz cosine wave

# Combine the two signals into a single EEG recording
eeg_data = signal1 + signal2

# Plot the synthetic EEG data
import matplotlib.pyplot as plt
plt.plot(time, eeg_data)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (uV)')
plt.show()