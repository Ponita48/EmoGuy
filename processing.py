import numpy as np
import time


def LBP1D(data=None):
	if data is not None:
		result = []
		for col in data.T:
			mid = 4
			# return len(col)
			if str(col[0]) == "Timestamp":
				print "Skipping Timestamp"
				continue
			sensor = []
			while mid < len(col):
				binary_num = ""
				for x in xrange(1,5):
					binary_num += str(int(col[mid] >= col[mid-x]))
				for x in xrange(1,5):
					binary_num += str(int(col[mid] >= col[mid+x]))
				sensor.append(binary_to_int(binary_num))
				mid += 9
			result.append(sensor)
	return np.array(result)

def binary_to_int(num):
	return int(num, 2)