#!/usr/bin/python

import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

Data = open(r"Data.txt", "r")

Amount = []
Freq = []
alpha = []
acnt = 0
sortedLikelihood = []
LMax = 0

count = 0

for line in Data:

    splittedLine = line.split()

    Amount.append(int(splittedLine[0]))
    Freq.append(int(splittedLine[1]))
    
    count = count + 1
Data.close()


def Sum(x, y):	#Function that calculates Sum of the frequencies and total accidents

	cnt = 0
	Output1 = 0
	Output2 = 0

	for len in x:

		Output1 = Output1 + x[cnt]
		Output2 = Output2 + x[cnt] * y[cnt]

		cnt = cnt + 1

	return(Output1, Output2)

for line in range (0,200):	#Variable Alpha

	acnt = acnt + 0.01
	alpha.append(float("%.2f" % acnt))


def deNum(amnt, freq):	#Function that calculates (x1)!*(x2)!*...*(xn)! 

	cnt = 0
	Output = 1

	for len in amnt:

		Output = Output * math.pow(math.factorial(amnt[cnt]), freq[cnt])
		cnt = cnt + 1

	return(Output)

def Likelihood(amnt, freq, a):	#Function that calculates Likelihood function

	Output = []
	cnt = 0	

	for len in a:

		Output.append(np.log(math.exp(-a[cnt]*Sum(freq, amnt)[0]) * pow(a[cnt], Sum(freq, amnt)[1])/deNum(amnt, freq)))
		
		cnt = cnt + 1

	return(Output)

sortedLikelihood = Likelihood(Amount, Freq, alpha)
sortedLikelihood.sort()
LM = sortedLikelihood[len(Likelihood(Amount, Freq, alpha))-1]

def LMax():	#Function that finds Maximum(LMax) and lnL from the graph

	Lcount = 0
	Output = 0
	lnL = 0

	for len in Likelihood(Amount, Freq, alpha):

		if (Likelihood(Amount, Freq, alpha)[Lcount] == LM):
			Output = Lcount * 0.01
	
		Lcount = Lcount + 1

	lnL = math.log(Lcount) - 1/2
	return(Output, lnL)



def drawGraph(x, y):	#Function that draws measured points
	
	plt.plot(x, y)

	plt.title("Log-Likelihood Plot for Accident")
	plt.xlabel("Lambda")
	plt.ylabel("Log-Likehood")

	plt.show()

print("Graph reaches max at Lambda = ", LMax()[0], ", and lnL is: ", "%.4f" % LMax()[1])
drawGraph(alpha, Likelihood(Amount, Freq, alpha))

