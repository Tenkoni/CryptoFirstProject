from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import csv
import csv
# Fixing random state for reproducibility


figu = plt.figure()
ax1 = figu.add_subplot(111)


resultsSHA1X = []
resultsSHA1Y = []
resultsSHA2X = []
resultsSHA2Y = []
resultsMD5X = []
resultsMD5Y = []



with open('Results/sha1.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			algoName = row
			line_count += 1
		else:
			resultsSHA1X.append(float(row[0]))
			#resultsSHA1Y.append(float(row[1]))
			line_count += 1
with open('Results/sha2.csv') as csv_fileTwo:
	csv_reader = csv.reader(csv_fileTwo, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			algoName = row
			line_count += 1
		else:
			resultsSHA2X.append(float(row[0]))
			#resultsSHA2Y.append(float(row[1]))
			line_count += 1
with open('Results/md5.csv') as csv_fileThree:
	csv_reader = csv.reader(csv_fileThree, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			algoName = row
			line_count += 1
		else:
			resultsMD5X.append(float(row[0]))
			#resultsMD5Y.append(float(row[1]))
			line_count += 1


forAx = []
forAx += resultsSHA1X
forAx += resultsSHA2X
forAx += resultsMD5X


#resultsSHA1X = resultsSHA1X[1:800]
#resultsSHA2X = resultsSHA2X[1:800]
#resultsMD5X  = resultsMD5X[1:800]
""""
forAy = []
forAy += resultsSHA1Y
forAy += resultsSHA2Y
forAy += resultsMD5Y
"""


ax1.scatter(range(len(resultsSHA1X)), resultsSHA1X, s =1,c = "r", alpha=0.5,label = "SHA1")
ax1.scatter(range(len(resultsSHA1X)), resultsSHA2X, s =1,c = "b", alpha=0.5, label = "SHA2")
ax1.scatter(range(len(resultsSHA1X)), resultsMD5X, s =1,c = "g", alpha=0.5, label = "MD5")
plt.ylabel('Hashing Time [s]')
plt.xlabel('N-th Test Vector')
plt.title('Diggesting time (lower Y is better)')


plt.axis([0,1000,min(forAx),0.0000028])
plt.legend(loc='upper right');
plt.show()
