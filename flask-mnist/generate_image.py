# -*- coding:utf-8 -*-

import pandas as pd
from scipy import misc

data_test = pd.read_csv('Data/test.csv')
X_test = data_test.values[2:3]

im = X_test.reshape((28,28))

misc.imsave('3.png',im)