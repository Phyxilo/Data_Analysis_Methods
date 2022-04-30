#!/usr/bin/python

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

Data = open(r"studentData.txt", "r")

mt1 = []
mt2 = []
fin = []
lab = []
hw = []
Att =[]

count = 0

for line in Data:

    splittedLine = line.split()

    mt1.append(int(splittedLine[0]))
    mt2.append(int(splittedLine[1]))
    fin.append(int(splittedLine[2]))
    lab.append(int(splittedLine[3]))
    hw.append(int(splittedLine[4]))
    Att.append(int(splittedLine[5]))
	
    count = count + 1
Data.close()

#print(mt1)

def mean(data):		#Mean Value function

	Sum = 0
	cnt = 0

	for len in data:
		Sum = Sum + data[cnt]
		cnt = cnt + 1
	return(Sum/cnt)


def median(data):	#Median function

	srtData = sorted(data)
	Output = srtData[int(len(srtData)/2)]

	return(Output)


def stdev(data):	#Standart Deviation function

	Sum = 0
	Dev = 0
	cnt = 0
	
	for len in data:
		Sum = Sum + (data[cnt] - mean(data))**2
		cnt = cnt + 1

	Dev = (1/(cnt-1) * Sum)**(1/2)
	return(Dev)


def skewdir(data):	#Skew Direction function
	

	if mean(data) <= median(data):
		skwDir = "Positive"
	else: skwDir = "Negative"

	return(skwDir)

dataType = Att		#Insert the name of the data that you want to evaluate Mean Value, Median, Standart Deviation and, Skew Direction. (Data Names: mt1, mt2, fin, lab, hw, Att)
 
print("Mean Value: " + str(mean(dataType)))
print("Median: " + str(median(dataType)))
print("Standart Deviation: " + str(stdev(dataType)))
print("Skew Direction: "+ str(skewdir(dataType)))
