#!/usr/bin/python

import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

r = 10000
rarray = []



for i in range(r):

	xn = np.random.uniform(0,1)
	rarray.append(float(xn))


def Funct(y):			#Function that calculates y axis of PDFs

	xA = []
	xB = []
	cnt = 0

	for i in range(r):

		xA.append(-np.log(y[cnt]*(1-math.exp(-2)))/2)
		xB.append(math.pow(y[cnt], 1/3))

		cnt = cnt + 1

	return(xA, xB)


def drawGraph(arrA, arrB):	#Function that draws measured points, errorbar and Least Square Fit
	
	plt.hist(arrA)
	plt.hist(arrB)
	
	plt.title("Monte Carlo Simulation")
	plt.xlabel("X-Axis")
	plt.ylabel("Y-Axis")

	plt.show()

drawGraph(Funct(rarray)[0], Funct(rarray)[1])
