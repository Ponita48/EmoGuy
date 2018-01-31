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
		self.bpass = None
		print("Membaca {}".format(self.name))

	def readData(self):
		with open(self.name, 'r') as f:
			reader = csv.DictReader(f)
			for row in reader:
				row_text = []
				for col in self.header:
					row_text = np.append(row_text, row[col])
				self.hasil = np.vstack((self.hasil, row_text))

	def dcOffset(self):
		i=1
		for column in self.hasil.T[1:]:
			self.hasil.T[i][1:] = self.hasil.T[i][1:].astype(np.float) - np.mean(column[1:].astype(np.float))	#DC Offset
			i+=1

	def fft(self):
		i = 1
		for column in self.hasil.T[1:]:
			if self.ibp is None:
				self.ibp = np.zeros(len(column) - 1)    
			# FFT
			fft = scipy.fft(self.hasil.T[i][1:])
			# print "ibp:", self.ibp.shape
			print "fft:", fft.shape
			for j in range(0, len(fft)):
				if j>=10:fft[j]=0
			self.ibp = np.vstack((self.ibp, np.array(scipy.ifft(fft))))
			i += 1


	def butter_bandpass_filter(self,data, lowcut, highcut, sampleRate, order=2):
		b, a = self.butter_bandpass(lowcut, highcut, sampleRate, order=order)
		y = lfilter(b, a, data.astype(np.float))
		return y

	def butter_bandpass(self,lowcut, highcut, sampleRate, order = 2):
		nyq = 0.5 * sampleRate
		low = lowcut / nyq
		high = highcut / nyq
		b, a = butter(order, [low, high], btype = 'band')
		return b, a

	def bandpass(self):
		i=1;
		for column in self.hasil.T[1:]:
			if self.bpass is None:
				self.bpass = np.zeros(len(column) - 1)
			bps = self.butter_bandpass_filter(self.hasil.T[i][1:],10,30,128,2)
			self.bpass= np.vstack((self.bpass, np.array(bps)))
			print "bpass:", self.bpass.shape
			i+=1

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
		plt.subplot(h,w,i);pylab.title("(II) Sinyal FFT")
		plt.plot(self.ibp.T)
		# i+=1

		pylab.figure(3)
		# for row in self.hasil.T[i:] :
		plt.subplots_adjust(hspace=.7)
		plt.subplot(h,w,i);pylab.title("(III) Sinyal Bandpass")
		plt.plot(self.bpass.T)

		plt.show()

		

	

hihi = preprocessing('csv/emotiv_values_2018-01-30 09-38-29.937000.csv')
hihi.readData()
hihi.dcOffset()
hihi.fft()
hihi.bandpass()
hihi.plot()



# print proc.LBP1D()