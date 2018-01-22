import csv
import time

import numpy as np
start = time.time()

data = np.array(['F3','FC5','F7','T7','P7','O1','O2','P8','T8','F8','AF4','FC6','F4','AF3'])

with open('hehe.csv', mode='r') as inputFile:
	reader = csv.reader(inputFile)
	#row_count = sum(1 for row in reader)
	#print row_count
	hasil = []
	hasilmax = 0
	for row in reader:
	 	temp = []
	 	for col in xrange(0,len(row)):
	 		if col%2 != 0:
	 			temp.append(row[col])
	 			hasilmax += 1
			if hasilmax < 5:
		 		hasil.append(temp)
	 		# print col
	# 	print temp
	# print max(hasil)

	data = np.append(data, hasil)
	print data
	res = time.time() - start
	print "Time Elapsed : %s" % res
	# print data
# for row in inputFile:
# 	tstamp = row["Timestamp"]
# 	F3 = row["F3 Value"]

# 	# print "%s\t|\t%s" % (tstamp, F3)
# 	print row
# 	break
