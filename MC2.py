#!/usr/bin/python

import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

r = 100
rarray = []
x = []
bins = 150
count = 0
srtP = []
fCut = 0

for i in range(r):


	xn = np.random.uniform(0, 1)
	rarray.append(float(xn))
	
	x.append(float(i/r))




def Funct(y):			#Function that calculates y axis of PDFs

	xA = []
	xB = []
	P = []

	for i in range(r):

		xA.append(-np.log(y[i]*(1-math.exp(-2)))/2)
		xB.append(math.pow(y[i], 1/3))
		P.append(-np.log(x[i] * 2/(1-math.exp(-2)) * math.exp(-2 * x[i]) + (1-x[i]) * 3 * x[i]**2))


	return(xA, xB, P)


srtP = Funct(rarray)[2]
srtP.sort()


for i in range(r):

	if Funct(rarray)[2][i] == srtP[0]:

		fCut = i/r


def drawGraph(arrA, arrB, arrP):	#Function that draws measured points, errorbar and Least Square Fit

	#plt.plot(x, arrP, markevery = [int(fCut*100)], marker = 7)
	plt.hist(arrA, int(bins), alpha=0.8)
	plt.hist(arrB, int(bins/5), facecolor='red', alpha=0.8)

	plt.xlim(0,1)
	
	plt.title("Monte Carlo Simulation")
	plt.xlabel("F")
	plt.ylabel("-ln(P)")

	plt.show()

#print("F-Cut: " , fCut)
drawGraph(Funct(rarray)[0], Funct(rarray)[1], Funct(rarray)[2])
