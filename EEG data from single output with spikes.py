import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#read in data
data = pd.read_csv("data.txt", sep=",")

#remove leading and trailing spaces from column names
data.columns = data.columns.str.strip()

#drop "Timestamp (Formatted)" column
data = data.drop(columns=["Timestamp (Formatted)"])

#create an array of zeros with the same length as the data
#make it have the same level as the data avg isntead of zero 0
spikes = (np.zeros(len(data)) + 1) * data["EXG Channel 0"].mean()
spikesBlue = (np.zeros(len(data)) + 1) * data["EXG Channel 0"].mean()


for i in range(1, len(data)-1):
    #check if the current value is greater than the previous and next values
    if data["EXG Channel 0"][i] > data["EXG Channel 0"][i-1]and data["EXG Channel 0"][i] > data["EXG Channel 0"][i+1] :
        #if so, set the current value to the mean of the previous and next values
        spikes[i] = (data["EXG Channel 0"][i-1] + data["EXG Channel 0"][i+1]) / 2

#this is the same as the above but for the positive spikes
for i in range(1, len(data)-1):
    threshold = data["EXG Channel 0"].max() * 0.95
    spikesBlue[data["EXG Channel 0"] > threshold] = data["EXG Channel 0"][data["EXG Channel 0"] > threshold]



#plot data
plt.figure()
plt.xlim(data["Timestamp"].min(), data["Timestamp"].max())
plt.plot(data["Timestamp"], data["EXG Channel 0"], label="EXG Channel 0")
plt.plot(data["Timestamp"], spikes, 'r-', label="Spikes")
plt.plot(data["Timestamp"], spikesBlue, 'b-', label="Spikes above threshold(95% of max))")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (uV)")
plt.legend()
plt.show()


