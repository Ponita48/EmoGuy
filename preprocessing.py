import csv

import numpy as np
import pywt

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

# print hasil

# normalisasi
i = 0
for column in hasil.T:
	hasil.T[i][1:] = hasil.T[i][1:].astype(np.float) - np.mean(column[1:].astype(np.float))
	i += 1

# print "\nsetelah normalisasi"
# print hasil

# wavelet
# for column in hasil.T:
# 	cA, cD = pywt.dwt(column, 'db5')