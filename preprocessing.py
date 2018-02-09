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
		start = time.time()
		self.name = name
		self.header = ['Timestamp', 'F3 Value','FC5 Value','F7 Value','T7 Value','P7 Value','O1 Value','O2 Value','P8 Value','T8 Value','F8 Value','AF4 Value','FC6 Value','F4 Value','AF3 Value']
		self.hasil = None
		self.ibp = None
		self.bpass = None
		self.bpassABG = None
		if self.name[-3:] == "csv" or self.name[-3:] == "CSV":
			print "Reading csv file: %s" % self.name
			self.readData()
			print time.time() - start
			self.dcOffset()
		elif self.name[-3:] == "txt" or self.name[-3:] == "TXT":
			print "Reading TXT file: %s" % self.name
			self.textRead()
			print time.time() - start

	def textRead(self):
		with open(self.name) as f:
			for row in f:
				if self.hasil is None:
					self.hasil = row.split()
					continue
				coba=row.split()
				self.hasil = np.vstack((self.hasil, np.array(coba)))

	def readData(self):
		self.hasil = np.array(self.header)
		with open(self.name, 'r') as f:
			reader = csv.DictReader(f)
			for row in reader:
				row_text = []
				for col in self.header:
					row_text = np.append(row_text, row[col])
				self.hasil = np.vstack((self.hasil, row_text))

	def dcOffset(self):
		i=1
		if self.name[-3:] == "csv" or self.name[-3:] == "CSV":
			for column in self.hasil.T[1:]:
				self.hasil.T[i][1:] = self.hasil.T[i][1:].astype(np.float) - np.mean(column[1:].astype(np.float))	#DC Offset
				i+=1
		elif self.name[-3:] == "txt" or self.name[-3:] == "TXT":
			for column in self.hasil.T[:]:
				self.hasil.T[i][:] = self.hasil.T[i][:].astype(np.float) - np.mean(column[:].astype(np.float))	#DC Offset
				i+=1


	def fft(self):
		if self.name[-3:] == "csv" or self.name[-3:] == "CSV":
			i = 1
			for column in self.hasil.T[1:]:
				if self.ibp is None:
					self.ibp = np.zeros(len(column) - 1)    
				# FFT
				fft = scipy.fft(self.hasil.T[i][1:])
				for j in range(0, len(fft)):
					if j>=10:fft[j]=0
				self.ibp = np.vstack((self.ibp, np.array(scipy.ifft(fft))))
				i += 1
		elif self.name[-3:] == "txt" or self.name[-3:] == "TXT":
			i = 0
			for column in self.hasil.T[:]:
				if self.ibp is None:
					self.ibp = np.zeros(len(column)) 
				# FFT
				fft = scipy.fft(self.hasil.T[i][:])
				for j in range(0, len(fft)):
					if j>=10:fft[j]=0
				self.ibp = np.vstack((self.ibp, np.array(scipy.ifft(fft))))
				i += 1

		self.ibp=self.ibp.T


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
		cutoff=[1,4,8,12,30]
		if self.name[-3:] == "csv" or self.name[-3:] == "CSV":
			i=1
			for column in self.hasil.T[1:]:
				if self.bpass is None:
					self.bpass = np.zeros(len(column) - 1)
				if self.bpassABG is None:
					self.bpassABG = np.zeros(len(column) - 1)
				bps = self.butter_bandpass_filter(self.hasil.T[i][1:],3,30,128,2)
				self.bpass= np.vstack((self.bpass, np.array(bps)))
				i+=1
			for x in range(0,4):
				bpastemp = self.butter_bandpass_filter(self.hasil.T[1][1:],cutoff[x],cutoff[x+1],128,2)
				if(np.array_equal(self.bpassABG,np.zeros(len(column)-1))):
					self.bpassABG = np.array(bpastemp)
				else:
					self.bpassABG= np.vstack((self.bpassABG,np.array(bpastemp)))
		elif self.name[-3:] == "txt" or self.name[-3:] == "TXT":
			i=0
			for column in self.hasil.T[:]:
				if self.bpass is None:
					self.bpass = np.zeros(len(column))
				if self.bpassABG is None:
					self.bpassABG = np.zeros(len(column) -1)
				bps = self.butter_bandpass_filter(self.hasil.T[i][:],0.5,30,500,2)
				self.bpass= np.vstack((self.bpass, np.array(bps)))
				i+=1
			for x in range(0,4):
				bpastemp = self.butter_bandpass_filter(self.hasil.T[1][:],cutoff[x],cutoff[x+1],128,2)
				if(np.array_equal(self.bpassABG,np.zeros(len(column)-1))):
					self.bpassABG = np.array(bpastemp)
				else:
					self.bpassABG= np.vstack((self.bpassABG,np.array(bpastemp)))
		self.bpass = self.bpass.T
		self.bpassABG = self.bpassABG.T

	def plot(self, data=None):
		plt.figure(1)
		plt.title("Data Plot")
		plt.plot(data.astype(np.float),'.-')
		
		plt.show()

		

	

# hihi = preprocessing('csv/emotiv_values_2018-01-30 09-38-29.937000.csv')
# hihi.fft()
# hihi.bandpass()
# hihi.plot(hihi.bpassABG)

# lala = preprocessing('1_rilex_close_pre_bipolar.TXT')

lala = preprocessing('aihihi.csv')
# lala.fft()
lala.bandpass()

# lala.plot(lala.hasil)
# lala.plot(lala.bpass.T[1])
# lala.plot(lala.bpassABG)
# lala.plot(lala.ibp)
lala.plot(processing.LBP1D(lala.bpass)[1])

# print proc.LBP1D()