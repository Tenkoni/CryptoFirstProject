from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import csv
import csv
# Fixing random state for reproducibility


figu = plt.figure()
ax1 = figu.add_subplot(111)


resultsPSSX = []
resultsPSSY = []
resultsDESX = []
resultsDESY = []
resultsDSAX = []
resultsDSAY = []


with open('Results/rsa_pss.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			algoName = row
			line_count += 1
		else:
			resultsPSSX.append(float(row[0]))
			resultsPSSY.append(float(row[1]))
			line_count += 1

with open('Results/des.csv') as csv_fileFive:
	csv_reader = csv.reader(csv_fileFive, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			algoName = row
			line_count += 1
		else:
			resultsDESX.append(float(row[0]))
			resultsDESY.append(float(row[1]))
			line_count += 1

with open('Results/dsa.csv') as csv_fileFive:
	csv_reader = csv.reader(csv_fileFive, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			algoName = row
			line_count += 1
		else:
			resultsDSAX.append(float(row[0]))
			resultsDSAY.append(float(row[1]))
			line_count += 1

resultsDESX = resultsDESX[0:160]
resultsDESY = resultsDESY[0:160]
forAx = []
forAx += resultsPSSX
#forAx += resultsDESX
forAx += resultsDSAX

forAy = []
forAy += resultsPSSY
#forAy += resultsDESY
forAy += resultsDSAY


ax1.scatter(resultsPSSX, resultsPSSY, s =10,c = "r", alpha=0.5, label = "RSA-PSS")
#ax1.scatter(resultsDESX, resultsDESY, s =10,c = "b", alpha=0.5, label = "DES")
ax1.scatter(resultsDSAX, resultsDSAY, s =10,c = "g", alpha=0.5, label = "DSA")


plt.ylabel('Signature Time [s]')
plt.xlabel('Verification Time [s]')
plt.title('Signature - Verification time (closer to the origin is better)')

plt.axis([min(forAx),max(forAx),min(forAy),max(forAy)])
#plt.axis([min(forAx)*1,max(forAx)*1,min(forAy)*1,max(forAy)*1])
plt.legend(loc='upper right');
plt.show()


