# Kelek Pantek

# Packages for analysis
import numpy as np
from sklearn import svm
from sklearn.externals import joblib
import preprocessing as pr

# Packages for visuals
import matplotlib.pyplot as plt
# Pickle package
import pickle

model = pickle.load(open('modelkuh.p','rb')) 

def muffin_or_cupcake(data):
    if(model['modelkuh'].predict([data]))==0:
        print('You\'re looking at a muffin recipe!')
    else:
        print('You\'re looking at a cupcake recipe!')


# Load Data
data = pr.readData("csv/gj-play.csv")
data = data.T[1:].T
for row in data:
	if(row[0]=="F3 Value"):
		continue
	muffin_or_cupcake(row)

# Let's get shit done!


print "ready"
# muffin_or_cupcake(42,21)