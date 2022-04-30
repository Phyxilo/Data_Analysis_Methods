#!/usr/bin/python

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

mu = 100
sigma = 15
num_bins = 10

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


n, bins, patches = plt.hist(mt1, num_bins, facecolor='blue', alpha=0.5)

plt.title(r"Midterm 1")

plt.show()

n, bins, patches = plt.hist(mt2, num_bins, facecolor='blue', alpha=0.5)

plt.title(r"Midterm 2")

plt.show()

n, bins, patches = plt.hist(fin, num_bins, facecolor='blue', alpha=0.5)

plt.title(r"Final")

plt.show()

n, bins, patches = plt.hist(lab, num_bins, facecolor='blue', alpha=0.5)

plt.title(r"Lab")

plt.show()

n, bins, patches = plt.hist(hw, num_bins, facecolor='blue', alpha=0.5)

plt.title(r"Homework")

plt.show()

n, bins, patches = plt.hist(Att, num_bins, facecolor='blue', alpha=0.5)

plt.title(r"Attendance")

plt.show()

