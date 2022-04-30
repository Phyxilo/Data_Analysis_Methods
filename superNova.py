#!/usr/bin/python

import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

Data = open(r"Data.txt", "r")

eventNum = []
intervalNum = []
expectedArray = []

count = 0

for line in Data:	#Adds data from the Data.txt into "eventNum" and "intervalNum" arrays

    splittedLine = line.split()

    eventNum.append(int(splittedLine[0]))
    intervalNum.append(int(splittedLine[1]))
	
    count = count + 1
Data.close()

def drawGraph(x, y, expct):	#Function that draws measured points
	
	plt.plot(x, expct, "ro")
	plt.bar(x, y, 1)

	plt.xlabel("Number of Events")
	plt.ylabel("Number of Intervals")

	plt.legend()

	plt.show()

def factorial(Num):	#Function that calculates factorial
	
	fact = 1

	for i in range(1, Num + 1):
		fact = fact * i

	return (fact)

def Lambda(event, inter):	#Function that calculates Lambda and total events

	count1 = 0
	count2 = 0
	Sum = 0	
	lmbd = 0
	
	for len in event:
		
		Sum = Sum + inter[count1]

		count1 = count1 + 1

	for len in event:

		lmbd = lmbd + (event[count2] * inter[count2])/Sum 
		
		count2 = count2 + 1


	return(lmbd, Sum)


def findExpct(event, lmbd, total):	#Function that find expected values for Poisson's Distribution

	Output = []
	count = 0

	for len in event:

		x = event[count]

		Output.append(int((total * math.exp(-lmbd) * pow(lmbd, event[count]))/(factorial(event[count]))))
		
		count = count + 1
	
	return(Output)

expectedArray = findExpct(eventNum, Lambda(eventNum, intervalNum)[0], Lambda(eventNum, intervalNum)[1])

print(expectedArray)

drawGraph(eventNum, intervalNum, expectedArray)
