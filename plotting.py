from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import csv
import csv
# Fixing random state for reproducibility
np.random.seed(19680801)

figu = plt.figure()
ax1 = figu.add_subplot(111)


N = 2816
resultsCTRX = []
resultsCTRY = []
resultsARCX = []
resultsARCY = []
resultsAESX = []
resultsAESY = []
resultsOFBX = []
resultsOFBY = []
resultsDESX = []
resultsDESY = []


with open('Results/aes_ctr.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			algoName = row
			line_count += 1
		else:
			resultsCTRX.append(float(row[0]))
			resultsCTRY.append(float(row[1]))
			line_count += 1
with open('Results/arc4.csv') as csv_fileTwo:
	csv_reader = csv.reader(csv_fileTwo, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			algoName = row
			line_count += 1
		else:
			resultsARCX.append(float(row[0]))
			resultsARCY.append(float(row[1]))
			line_count += 1
with open('Results/aes.csv') as csv_fileThree:
	csv_reader = csv.reader(csv_fileThree, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			algoName = row
			line_count += 1
		else:
			resultsAESX.append(float(row[0]))
			resultsAESY.append(float(row[1]))
			line_count += 1
with open('Results/aes_ofb.csv') as csv_fileFour:
	csv_reader = csv.reader(csv_fileFour, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			algoName = row
			line_count += 1
		else:
			resultsOFBX.append(float(row[0]))
			resultsOFBY.append(float(row[1]))
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


colors = np.random.rand(N)
#area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
resultsCTRX = resultsCTRX[:100]
resultsCTRY = resultsCTRY[:100]
resultsARCX = resultsARCX[:100]
resultsARCY = resultsARCY[:100]
resultsAESX = resultsAESX[:100]
resultsAESY = resultsAESY[:100]
resultsOFBX = resultsOFBX[:100]
resultsOFBY = resultsOFBY[:100]
resultsDESX = resultsDESX[:100]
resultsDESY = resultsDESY[:100]


forAx = []
forAx += resultsCTRX
forAx += resultsARCX
forAx += resultsAESX
forAx += resultsOFBX
#forAx += resultsDESX

forAy = []
forAy += resultsCTRY
forAy += resultsARCY
forAy += resultsAESY
forAy += resultsOFBY
#forAy += resultsDESY

ax1.scatter(resultsARCX, resultsARCY, s =10,c = "r", alpha=0.5,label = "RC4")
ax1.scatter(resultsCTRX, resultsCTRY, s =10,c = "b", alpha=0.5, label = "AES CTR")
ax1.scatter(resultsAESX, resultsAESY, s =10,c = "g", alpha=0.5, label = "AES")
ax1.scatter(resultsOFBX, resultsOFBY, s =10,c = "y", alpha=0.5, label = "OFB")
ax1.scatter(resultsDESX, resultsDESY, s =1,c = "#eabfb9", alpha=0.5, label = "DES- (Too big for display)")
plt.ylabel('Encryption Time [s]')
plt.xlabel('Decryption Time [s]')
plt.title('Encryption and Decryption time (closer to the origin is better)')
plt.axis([min(forAx)*1,.000019,min(forAy)*1,.000019])
#plt.axis([min(forAx)*1,max(forAx)*1,min(forAy)*1,max(forAy)*1])
plt.legend(loc='upper right');
plt.show()

whosFast = [0,0,0,0]
for i in range(99):
	a = [resultsCTRX[i],resultsARCX[i],resultsOFBX[i],resultsAESX[i]]
	whosFast[a.index(min(a))] += 1

