import csv
import time

import numpy as np
import scipy, pylab
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
from scipy.fftpack import rfft, irfft, fftfreq

import processing

class preprocessing:
	
	def __init__(self, name):
		self.name = name
		self.header = ['Timestamp', 'F3 Value','FC5 Value','F7 Value','T7 Value','P7 Value','O1 Value','O2 Value','P8 Value','T8 Value','F8 Value','AF4 Value','FC6 Value','F4 Value','AF3 Value']
		self.hasil = np.array(self.header)
		self.ibp = None
		print("Membaca {}".format(self.name))

	def readData(self):
		with open(self.name, 'r') as f:
			reader = csv.DictReader(f)
			for row in reader:
				row_text = []
				for col in self.header:
					row_text = np.append(row_text, row[col])
				self.hasil = np.vstack((self.hasil, row_text))

	def fft(self):
		i = 1
		for column in self.hasil.T[1:]:
			if self.ibp is None:
				self.ibp = np.zeros(len(column) - 1)
			self.hasil.T[i][1:] = self.hasil.T[i][1:].astype(np.float) - np.mean(column[1:].astype(np.float))	#DC Offset    
			# FFT
			fft = scipy.fft(self.hasil.T[i][1:])
			print "ibp:", self.ibp.shape
			print "fft:", fft.shape
			for j in range(0, len(fft)):
				if j>=10:fft[j]=0
			self.ibp = np.vstack((self.ibp, np.array(scipy.ifft(fft))))
			i += 1

	def plot(self):
		print "ibp: ", self.ibp.shape
		print "hasil: ", self.hasil.shape
		i=1
		j=1
		h,w=1,1
		plt.figure(1)

		# for row in self.hasil.T[i:] :
		plt.subplots_adjust(hspace=.7)

		plt.subplot(h,w,i);plt.title("(I) Sinyal Asli")
		plt.plot(self.hasil[:][1:])
			# i+=1

		# i=1
		pylab.figure(2)
		# for row in self.hasil.T[i:] :
		plt.subplots_adjust(hspace=.7)
		plt.subplot(h,w,i);pylab.title("(I) Sinyal FFT")
		plt.plot(self.ibp.T)
		i+=1
		plt.show()

hihi = preprocessing('csv/emotiv_values_2018-01-30 09-38-29.937000.csv')
hihi.readData()
hihi.fft()

hihi.plot()



# print proc.LBP1D()