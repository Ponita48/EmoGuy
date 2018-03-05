import numpy as np
import time
import matplotlib.pyplot as plt

import preprocessing as prp

name = 'csv/cf-rilek.csv'
hasil = prp.readData(name)
timestamp = hasil.T[0]
hasilLen = len(hasil)
hasil = hasil.T[1:].T

name = "csv/cf-play.csv"
hasil2 = prp.readData(name)
timestamp2 = hasil2.T[0]
hasil2Len = len(hasil2)
hasil2 = hasil2.T[1:].T

hasil = np.vstack((hasil, hasil2[1:]))

target = np.zeros(hasilLen-1)
target = np.append(target, np.ones(hasil2Len-1))

from sklearn.decomposition import FastICA
hasil = prp.dcOffset(hasil)
ica = FastICA()
S_ = ica.fit_transform(hasil)
A_ = ica.mixing_


from sklearn import svm
import time
print "Start Learning"
start = time.time()
model = svm.SVC(kernel='linear')
model.fit(hasil, target)
print "Learning Finished on", time.time() - start, "s"

import pickle
modelkuh = {'modelkuh': model}
# Pickle
pickle.dump(modelkuh, open("modelkuh.p", "wb"))
pickle.dumps(modelkuh)

# print target
# print len(target)

