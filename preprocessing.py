import csv

import numpy as np
# import pywt
from scipy.signal import butter, lfilter
from scipy.fftpack import rfft, irfft, fftfreq

#get_raw_data
header = ['F3','FC5','F7','T7','P7','O1','O2','P8','T8','F8','AF4','FC6','F4','AF3']
with open('aihihi.csv', mode='r') as input_file:
	# Baca file csv
	reader = csv.reader(input_file)
	# inisialisasi array awal serta header
	hasil = np.array(header)
	# untuk menghilangkan header yang ada di csv
	First = True
	# looping ke bawah 
	for row in reader:
		# data per baris (ambil data yang penting (sinyal) )
		temp = []
		for col in xrange(0,len(row)):
			if col%2 != 0:
				# kalo baris pertama(header) maka di break
				if First:
					break
				# kalo udah 14 item maka break
				if len(temp) > 13:
					break
				# digabung biar bisa jadi array
				temp = np.append(temp, row[col])

		# kalo bukan pertama maka ditambah ke array, kalo pertama maka set jadi false
 		if not First:
			hasil = np.vstack((hasil, np.array(temp)))
		else:
			First = False

# normalisasi
# Sample rate dan cutoff (dalam hz)
fs = 1000.0
lowcut = 130.0
highcut = 170.0
N = 256
T = 1/256
order = 5

# (DC offset)
i = 0
for column in hasil.T:
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

