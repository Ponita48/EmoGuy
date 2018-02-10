import numpy as np
import time

import preprocessing as prp

name = 'aihihi.csv'
hasil = prp.readData(name)
header = hasil[0][0] == "Timestamp"
hasil = prp.dcOffset(hasil, header)
# print hasil[1:].T[1:]
# prp.plot(hasil[1:].T[1:].T)