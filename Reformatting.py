# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 22:36:58 2017

@author: Sven Geboers
"""
import numpy
import matplotlib.pyplot as plt

data = numpy.genfromtxt('Data/1',delimiter = ',')
length = len(data)
data = data[:]

## Velocity components ##
U = data[:,1]
V = data[:,2]
W = data[:,3]
##=====================##
SOS = data[:,5] #Speed of Sound
OtherData = data[:,6]   # not sure what it is
index = data[:,9] # Index number of the data
timestamp = data[:,10]


plt.scatter(index,SOS)
plt.show()
print (timestamp)
