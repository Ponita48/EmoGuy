import csv
import time

import numpy as np
import scipy, pylab
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
from scipy.fftpack import rfft, irfft, fftfreq

import processing

start = time.time()
#get_raw_data
header = ['Timestamp', 'F3 Value','FC5 Value','F7 Value','T7 Value','P7 Value','O1 Value','O2 Value','P8 Value','T8 Value','F8 Value','AF4 Value','FC6 Value','F4 Value','AF3 Value']
hasil = np.array(header)
with open('emotiv_values_2018-01-26 08-37-47.436000.csv', 'r') as f:
	reader = csv.DictReader(f)
	for row in reader:
		row_text = []
		for col in header:
			row_text = np.append(row_text, row[col])
		hasil = np.vstack((hasil, row_text))

# normalisasi
# Sample rate dan cutoff (dalam hz)

# (DC offset)
ibp = np.zeros(len(hasil)-1)
# print len(hasil)
i = 1
for column in hasil.T[1:]:
    hasil.T[i][1:] = hasil.T[i][1:].astype(np.float) - np.mean(column[1:].astype(np.float))	
    fft = scipy.fft(hasil.T[i][1:])
    bp = fft[:]
    for j in range(len(bp)):
        if j>=10:bp[j]=0
    ibp = np.vstack((ibp, np.array(scipy.ifft(bp))))
    i += 1
# FFT
ibp = ibp[1:]
ibp = ibp.T

aihihi = processing.LBP1D(ibp)

print "time: ", time.time() - start

# print len(ibp[0])
# exit()

i = 1

plt.figure(1)
for row in aihihi:
    plt.tick_params(
        axis='both',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off',
        left='off',
        right='off',         # ticks along the top edge are off
        labelbottom='off') # labels along the bottom edge are off
    plt.subplot(7, 2, i)
    plt.plot(aihihi[i-1], '-')
    i+=1
plt.show()
