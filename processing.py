import numpy as np
import time
import matplotlib.pyplot as plt

import preprocessing as prp

name = 'csv/cf-rilek.csv'
hasil = prp.readData(name)
header = hasil[0][0] == "Timestamp"
hasil = prp.dcOffset(hasil, True)
# name2 = 'csv/cf-play.csv'
# hasil2 = prp.readData(name2)
# hasil2 = prp.dcOffset(hasil2, True)
# print hasil[1:].T[1:]
# prp.plot(hasil[1:].T[1:].T)

bpass,bpassABG=prp.bandpass(hasil,True)

# hasil=prp.fft(hasil,True)
# hasil2,hasilabg2=prp.bandpass(hasil2,True)

# print hasil

# hasil = prp.wavelet(hasil)
# hasil2 = prp.wavelet(hasil2)


plt.figure(1)
plt.subplot(111)
plt.plot(hasil.T[0])


# plt.subplot(212)
# plt.plot(hasil2.T[0])
plt.show()
