import pandas as pd
import matplotlib.pyplot as plt

#read in data
data = pd.read_csv("data.txt", sep=",")

#remove leading and trailing spaces from column names
data.columns = data.columns.str.strip()

#drop "Timestamp (Formatted)" column
data = data.drop(columns=["Timestamp (Formatted)"])


#plot data
plt.figure()
plt.xlim(data["Timestamp"].min(), data["Timestamp"].max())
for i in range(4):
    plt.plot(data["Timestamp"], data["EXG Channel {}".format(i)], label="EXG Channel {}".format(i))
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (uV)")
plt.legend()
plt.show()


