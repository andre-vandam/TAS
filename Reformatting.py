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

U = data[:,1]
V = data[:,2]
W = data[:,3]
SOS = data[:,5]
OtherData = data[:,6]
index = data[:,9]
timestamp = data[:,10]


plt.scatter(index,SOS)
plt.show()