#!/usr/bin/python

import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

Data = open(r"Data.txt", "r")

X = []
Y = []
Sigma = []
Id = []
count = 0


for line in Data:

	splittedLine = line.split()

	X.append(float(splittedLine[0]))
	Y.append(float(splittedLine[1]))    
	Sigma.append(float(splittedLine[2]))
	Id.append(float(1))

	count = count + 1
Data.close()

def Sum(x, y):	#Function that calculates Sum of the frequencies and total accidents

	cnt = 0
	Output1 = 0

	for len in x:

		Output1 = Output1 + x[cnt] * y[cnt]

		cnt = cnt + 1

	return(Output1)


def Alpha(x, y):	#Function that calculates Alpha
	
	Output = 0

	Output = (Sum(y, Id) * Sum(x, x) - Sum(x, y) * Sum(x, Id)) / (4 * Sum(x, x) - math.pow(Sum(x, Id), 2))

	return(Output)

def Beta(x, y):		#Function that calculates Beta

	Output = 0

	Output = (4 * Sum(x, y) - Sum(x, Id) * Sum(y, Id)) / (4 * Sum(x, x) - math.pow(Sum(x, Id), 2))

	return(Output)

def Line(x, y):		#Function that find y values of the fit

	cnt = 0
	Output = []

	for len in x:

		Output.append((float(Alpha(x, y)) + X[cnt] * float(Beta(x, y))))

		cnt = cnt + 1

	return(Output)

def sigma(x, y):

	Output = 0

	Output = Sum(x, x) / (4 * Sum(x, x) - math.pow(Sum(x, Id), 2))

	return(Output)

def chiSqr(x, y):	#Function that calculates ChiSquare

	Output = 0
	cnt = 0
	
	for len in X:

		Output = Output + (Line(x, y)[cnt] -1 - Beta(x, y) * X[cnt]) / (Sigma[cnt])
		cnt = cnt + 1

	return(Output)
	
def drawGraph(x, y):	#Function that draws measured points, errorbar and Least Square Fit
	
	plt.errorbar(x, y, Sigma)
	plt.plot(x ,Line(x, y))

	plt.title("Least Square")
	plt.xlabel("X-Axis")
	plt.ylabel("Y-Axis")

	plt.show()

print("ChiSquare is " + str("%.4f" % chiSqr(X, Y)) + " and degrees of freedom is 2 ")
print("Since, Chi Square / DOF = " + str("%.4f" % (chiSqr(X, Y)/2)) + " < 1 " + "It is a good fit")
drawGraph(X, Y)
