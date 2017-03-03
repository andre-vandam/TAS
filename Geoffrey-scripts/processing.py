import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from math import sqrt

filename = "Gill Log [WM1]-4"

# Data array creation from data.txt
data = np.genfromtxt(filename, delimiter =',', skip_header=5, skip_footer=1, dtype=str)

# Time stamp string sectioning (removal of date)
for i in range(len(data[:,10])):
    time = data[i,10]
    time = time[11:]
    data[i,10] = time

# Function to calculate time interval between two time-stamps
def timedifference(t1, t2):
    t1 = t1
    t2 = t2

    # Calculation of time interval between two time-stamps
    dh = float(t2[:-6]) - float(t1[:-6])
    dm = float(t2[2:-3]) - float(t1[2:-3])
    ds = float(t2[5:]) - float(t1[5:])
    Dt = dh*60*60 + dm*60 + ds #[s]
    return Dt

# Lambda Function to calculate magnitude of vector from components.
g = lambda x,y,z: sqrt(float(x)**2+float(y)**2+float(z)**2)

t = PrettyTable(['I.D.',"Vx", "Vy", "Vz", "Time", "S.O.S."])

time = []

Vlist =[]

for i in range(len(data[:,1])):
    time.append(timedifference(data[0,10], data[i,10]))

# Conversion of velocity components into float, and ignoring of empty cells.
for j in range(3):
    for i in range(len(data[:,1+j])):
        if data[i,1+j] == '':
            data[i,1+j] = 0

        # Should the cell be empty, the value 0 will be assigned
        elif data[i,1+j] != '':
            data[i,1+j] = float(eval(data[i,1]))

# Rows added for display in the pretty table
for i in range(len(data[:,1])):
    t.add_row([i, data[i,1], data[i,2], data[i,3], data[i,10], data[i,5]])

# Calculation of the wind vector through u,v,w components.
for i in range(len(data[:,1])):
    V = g(data[i,1], data[i,2], data[i,3])
    Vlist.append(V)

plt.plot(time, Vlist)
plt.show()
print(t)

