#!/usr/bin/python
import math

Value = input("Value: ")
#intValue = int(Value)

inputArr = Value.split(",")

for x in range (len(inputArr)):

	inputArr[x] = int(inputArr[x])

inputArr.sort(reverse = True)

def primeGen(limit):

	numArr = []
	primeArr = []
	prime = 0

	for i in range (2, limit+1):

		numArr.append(i)

	for x in range (len(numArr)):

		isPrime = True

		for y in range (1, numArr[x]-1):

			prime = numArr[x]%(numArr[x]-y)

			if (prime == 0): isPrime = False

		if (isPrime == True): primeArr.append(numArr[x])
			
	return(primeArr)


def LCM(Value):

	primeArr = []
	x = 0
	LCMmult = 1

	primeArr = primeGen(Value[0])

	while True:

		while True:

			mult = 1
			isDiv = False

			for y in range (len(Value)):

				if (Value[y]%primeArr[x] == 0):
					Value[y] = Value[y]/primeArr[x]
					isDiv = True

				mult *= Value[y]%primeArr[x]
				#print(Value, "Multiplier: ", LCMmult, "Prime: ", primeArr[x])

			if (isDiv):LCMmult *= primeArr[x]

			if (mult != 0):break 

		x += 1

		totalMult = 1

		for i in range (len(Value)):

			totalMult *= Value[i]
			
		if (totalMult == 1):break
		
	return(LCMmult)

def GCF(Value):

	Mult = 1
	Output = 0

	for x in range (len(Value)):

		Mult *= abs(Value[x])

	Output = Mult/LCM(Value)
	print(Mult)
	return (Output)

print(LCM(inputArr))

