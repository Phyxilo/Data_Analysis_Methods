#!/usr/bin/python

import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

Data = open(r"Data.txt", "r")

MT1 = []
MT2 = []
lineNum = []
dataLen = 0
df = 1 #Regression degrees of freedom is 1 since only mean calculated from the data

count = 0

for line in Data:

    splittedLine = line.split()

    MT1.append(int(splittedLine[0]))
    MT2.append(int(splittedLine[1]))
    lineNum.append(count)
    
    count = count + 1
Data.close()

dataLen = len(lineNum)

def drawGraph(x, y, fitedX, fitedY):	#Function that draws measured points
	
	plt.plot(x, y, "o")
	plt.plot(fitedX, fitedY, "r")

	plt.title("Midterm 1")
	plt.xlabel("Students")
	plt.ylabel("Grades")

	plt.show()

def mean(data):		#Mean Value function

	Sum = 0
	cnt = 0

	for len in data:
		Sum = Sum + data[cnt]
		cnt = cnt + 1
	return(Sum/cnt)



def S(x, y):		#Function that calculates Least Square Estimators

	cnt = 0
	Mult = 0
	Sumx = 0
	Sumy = 0
	Output = []


	for len in x:
		
		Mult = Mult  + (x[cnt] * y[cnt])

		Sumx = Sumx + x[cnt]
		Sumy = Sumy + y[cnt]

		cnt = cnt + 1

	Output = Mult - (Sumx * Sumy) / dataLen

	return(Output)

def lineFit(x, y):	#Function that calculates fitted X Values , Alpha and Beta

	Beta = 0
	Alpha = 0
	Output = []
	cnt = 0
	
	Beta = S(y, x) / S(y, y)
	Alpha = mean(y) - Beta * mean(x)

	for len in x:

		Output.append(Alpha + Beta * x[cnt])

		cnt = cnt + 1

	return(Output)

def SS(x, y):		#Function that calculates SSE, SSR, Total SS, MSR, MSE

	ssr = 0
	sse = 0	

	ssr = S(x, y)**2 / S(x, x)
	sse = S(y, y) - ssr

	msr = ssr/df
	mse = sse/(dataLen - 2)

	return(ssr, sse ,S(y, y), msr ,mse)

print("SSE : ", SS(lineNum, MT1)[0] , "SSR: ", SS(lineNum, MT1)[1], "Total SS: ", SS(lineNum, MT1)[2], "MSR: ", SS(lineNum, MT1)[3], "MSE: ", SS(lineNum, MT1)[4])
print("r^2: ", SS(lineNum, MT1)[1]/SS(lineNum, MT1)[2])

drawGraph(lineNum, MT1, lineNum, lineFit(lineNum, MT1))
drawGraph(lineNum, MT2, lineNum, lineFit(lineNum, MT2))
