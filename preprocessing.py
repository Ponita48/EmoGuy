import csv
import time

import numpy as np
import scipy, pylab
import matplotlib.pyplot as plt
import pywt
from scipy.signal import butter, lfilter
from scipy.fftpack import rfft, irfft, fftfreq

header = ['Timestamp', 'F3 Value','FC5 Value','F7 Value','T7 Value','P7 Value','O1 Value','O2 Value','P8 Value','T8 Value','F8 Value','AF4 Value','FC6 Value','F4 Value','AF3 Value']
vstack = np.vstack
def readData(name=None):
	print "Reading from %s data" % name[-3:]
	if name[-3:] == "csv" or name[-3:] == "CSV":
		hasil = np.array(header)
		with open(name, 'r') as f:
			reader = csv.DictReader(f)
			for row in reader:
				row_text = []
				for col in header:
					row_text = np.append(row_text, row[col])
				hasil = vstack((hasil, row_text))
	elif name[-3:] == "txt" or name[-3:] == "TXT":
		with open(name) as f:
			for row in f:
				if hasil is None:
					hasil = row.split()
					continue
				coba=row.split()
				hasil = vstack((hasil, np.array(coba)))
	return hasil

def dcOffset(data, have_header=True):
	i=1
	data = data[have_header:].T.astype(np.float)
	# print data
	mean = np.mean(data)
	data = data - mean;	
	data = data.T
	# for column in data.T[have_header:]:
	# 	data.T[i][have_header:] = data.T[i][have_header:].astype(np.float) - np.mean(column[have_header:].astype(np.float))	#DC Offset
	# 	i+=1
	return data

def fft(data, have_header=True):
	ibp=None
	if have_header:
		i = 1
	else:
		i = 0
	for column in data.T[have_header:]:
		if ibp is None:
			ibp = np.zeros(len(column) - have_header)    
		# FFT
		fft = scipy.fft(data.T[i][have_header:])
		for j in range(0, len(fft)):
			if j>=10:fft[j]=0
		ibp = vstack((ibp, np.array(scipy.ifft(fft))))
		i += 1
	ibp=np.array(ibp)
	return ibp.T

def butter_bandpass_filter(data, lowcut, highcut, sampleRate, order=2):
	b, a = butter_bandpass(lowcut, highcut, sampleRate, order=order)
	y = lfilter(b, a, data.astype(np.float))
	return y

def butter_bandpass(lowcut, highcut, sampleRate, order = 2):
	nyq = 0.5 * sampleRate
	low = lowcut / nyq
	high = highcut / nyq
	b, a = butter(order, [low, high], btype = 'band')
	return b, a

def bandpass(data, have_header=True):
	bpass = np.zeros(len(data.T[0])-1)
	bpassABG = np.zeros(len(data.T[0])-1)
	cutoff=[1,4,8,12,30]
	#print len(data.T[0])	
	for column in data.T:
		bps = butter_bandpass_filter(column[have_header:],14,30,128,2)
		bpass= vstack((bpass, np.array(bps)))
	# for x in range(0,4):
	# 	bpastemp = butter_bandpass_filter(data.T[1][have_header:],cutoff[x],cutoff[x+1],128,2)
	# 	if(np.array_equal(bpassABG,np.zeros(len(column)-1))):
	# 		bpassABG = np.array(bpastemp)
	# 	else:
	# 		bpassABG= vstack((bpassABG,np.array(bpastemp)))
	bpass = bpass[1:].T
	bpassABG = bpassABG.T
	return bpass, bpassABG

def bandpassX(data, have_header=True):
	data = data.T
	bpass = np.zeros(len(data[0])-1)
	bpassABG = []
	cutoff=[1,4,8,12,30]
	#print len(data.T[0])	
	for column in data:
		bps = butter_bandpass_filter(column[have_header:],1,30,128,2)
		bpass= np.vstack((bpass, np.array(bps)))
	
	bpassX = np.zeros(len(data[0])-1)
	for column in data:
		bps = butter_bandpass_filter(column[have_header:],1,4,128,2)
		bpassX= np.vstack((bpassX, np.array(bps)))
	bpassABG.append(bpassX[1:].T)
	bpassX = np.zeros(len(data[0])-1)
	for column in data:
		bps = butter_bandpass_filter(column[have_header:],4,7,128,2)
		bpassX= np.vstack((bpassX, np.array(bps)))
	bpassABG.append(bpassX[1:].T)
	bpassX = np.zeros(len(data[0])-1)
	for column in data:
		bps = butter_bandpass_filter(column[have_header:],8,15,128,2)
		bpassX= np.vstack((bpassX, np.array(bps)))
	bpassABG.append(bpassX[1:].T)
	bpassX = np.zeros(len(data[0])-1)
	for column in data:
		bps = butter_bandpass_filter(column[have_header:],16,31,128,2)
		bpassX= np.vstack((bpassX, np.array(bps)))
	bpassABG.append(bpassX[1:].T)
	# for x in range(0,4):
	# 	bpastemp = butter_bandpass_filter(data.T[1][have_header:],cutoff[x],cutoff[x+1],128,2)
	# 	if(np.array_equal(bpassABG,np.zeros(len(column)-1))):
	# 		bpassABG = np.array(bpastemp)
	# 	else:
	# 		bpassABG= vstack((bpassABG,np.array(bpastemp)))
	bpass = bpass[1:].T
	# bpassABG = bpassABG.T
	return bpass, bpassABG

def plot(data=None):
	plt.figure(1)
	plt.title("Data Plot")
	plt.plot(data.astype(np.float))
	
	plt.show()

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
				sensor.append(int(binary_num, 2))
				mid += 1
			result.append(sensor)
		return np.array(result)
	else:
		return "Data Tidak Boleh Kosong"

def wavelet(data=None):
	if data is not None:
		is_raw = False
		if data[0][0] == "Timestamp":
			data = data[1:]
			is_raw = True
		ret_val = np.zeros(len(data.T[0])+1)
		for col in data.T:
			if is_raw:
				is_raw = False
				continue
			coeffs = pywt.wavedec(col, 'db1', level=5)
			recon = pywt.waverec(coeffs, 'db1')
			ret_val = vstack((ret_val, np.array(recon)))
		return ret_val[1:].T

"""
TODO: pake keras? drivernya (CUDA) gede pizun :((( kalo gak pake, harus bikin LSTM manual

"""