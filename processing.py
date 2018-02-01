import numpy as np
import time

import pywt

def LBP1D(data=None):
	if data is not None:
		result = []
		for col in data.T:
			mid = 0
			if str(col[0]) == "Timestamp":
				print "Skipping Timestamp"
				continue
			sensor = []
			while mid < len(col):
				binary_num = ""
				for x in xrange(1,5):
					if mid-x < 0:
						binary_num += '0'
					else:
						binary_num += str(int(col[mid] >= col[mid-x]))
				for x in xrange(1,5):
					if mid+x >= len(col):
						binary_num += '0'
					else:
						binary_num += str(int(col[mid] >= col[mid+x]))
				sensor.append(binary_to_int(binary_num))
				mid += 1
			result.append(sensor)
		return np.array(result)
	else:
		return "Data Tidak Boleh Kosong"

def binary_to_int(num):
	return int(num, 2)

def wavelet(data=None):
	if data is not None:
		is_raw = False
		if data[0][0] == "Timestamp":
			data = data[1:]
			is_raw = True
		ret_val = np.zeros(len(data.T[0]))
		for col in data.T:
			if is_raw:
				is_raw = False
				continue
			coeffs = pywt.wavedec(col, 'db1', level=5)
			recon = pywt.waverec(coeffs, 'db1')
			ret_val = np.vstack((ret_val, np.array(recon)))
		return ret_val[1:]