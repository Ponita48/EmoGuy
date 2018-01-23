import csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import pywt
from scipy.signal import butter, lfilter
from scipy.fftpack import rfft, irfft, fftfreq

#get_raw_data
header = ['Timestamp', 'F3 Value','FC5 Value','F7 Value','T7 Value','P7 Value','O1 Value','O2 Value','P8 Value','T8 Value','F8 Value','AF4 Value','FC6 Value','F4 Value','AF3 Value']
hasil = np.array(header)
hasil = np.vstack((hasil, pd.read_csv('aihihi.csv', skipinitialspace=True, usecols=header).as_matrix()))

# normalisasi
# Sample rate dan cutoff (dalam hz)
fs = 1000.0
lowcut = 130.0
highcut = 170.0
N = 256
T = 1/256
order = 5

# (DC offset)
i = 1
for column in hasil.T[1:]:
	hasil.T[i][1:] = hasil.T[i][1:].astype(np.float) - np.mean(column[1:].astype(np.float))	
	i += 1

# W = fftfreq(hasil.T[1][1], d=1)

# ybpf = butter_bandpass_filter(y,lowcut,highcut,N,order=2) 


# Fungsi Bandpass
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


print '--------'
print hasil.T[1][1]


# print "\nsetelah normalisasi"
# print hasil

# wavelet
# for column in hasil.T:
# 	cA, cD = pywt.dwt(column, 'db5')

