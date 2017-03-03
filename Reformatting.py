# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 22:36:58 2017

@author: Sven Geboers
"""
import numpy as np
import matplotlib.pyplot as plt
import re


convert = lambda time: re.sub(b':',b'',time[(len(time)-7):])
data= np.genfromtxt('Data/1',delimiter = ',', converters ={10:convert})
print (data)


# print(data)
def TransformTime (data):

    time = data[:,10]
    t0 = time[0]
    print("time")
    print(time)
    t0h = t0[0]
    t0m= t0[1:3]
    t0s=t0[3:5]
    for i in range(len(time)):
        hour = time[i][0]
        minute = time[i][1:3]
        second =time[i][3:5]
        dt = (hour-t0h)*60 + (minute-t0m)*60 + (second-t0s)
        time [i]=dt
    return time

# print(TransformTime(data))
# ## Velocity components ##
# U = data[:,1]
# V = data[:,2]
# W = data[:,3]
# ##=====================##
# SOS = data[:,5] #Speed of Sound
# OtherData = data[:,6]   # not sure what it is
# index = data[:,9] # Index number of the data
# timestamp = data[:,10]


# plt.scatter(index,SOS)
# plt.show()
# print (timestamp)
