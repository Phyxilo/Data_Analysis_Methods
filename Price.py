#!/usr/bin/python

import math

Data = open(r"Data.txt", "r")

Sample = []
SellPrice = []
M2 = []
t = 1.761		#Degrees of Freedom is 15-1 = 14 and confidence interval is 95% so t = 1.761

count = 0

for line in Data:

    splittedLine = line.split()

    Sample.append(int(splittedLine[0]))
    SellPrice.append(int(splittedLine[1]) * 1000)
    M2.append(int(splittedLine[2]))
    
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



def stdev(data):	#Standart Deviation function

	Sum = 0
	Dev = 0
	cnt = 0
	
	for len in data:
		Sum = Sum + (data[cnt] - mean(data))**2
		cnt = cnt + 1

	Dev = (1/(cnt-1) * Sum)**(1/2)
	return(Dev)

def PerM2(price, Meter2):	#Function that calculate House sell price per meter square for each house
	
	cnt = 0
	Output = []
	
	for len in price:
		Output.append(price[cnt]/Meter2[cnt])
		cnt = cnt + 1

	return(Output)

def TDis(data):		#Function that calculates T Distribution
	
	x = 0

	x = t * (stdev(data)/len(data)**(1/2))
	
	Output = (mean(data) - x , (mean(data) + x))

	return(Output)
print("Estimated Sell Price for House in TL: ",TDis(SellPrice))
print("Estimated Sell Price for House Per Meter Square in TL/m^2: ",TDis(PerM2(SellPrice,M2)))
