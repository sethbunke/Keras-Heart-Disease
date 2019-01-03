import sys
import pandas as pd
import numpy as np
import sklearn
import matplotlib
import keras

#https://www.safaribooksonline.com/library/view/machine-learning-for/9781789536591/197f4fea-ca00-4a3a-b98f-f625a54b975a.xhtml

print('Python: {}'.format(sys.version))
print('Pandas: {}'.format(pd.__version__))
print('Numpy: {}'.format(np.__version__))
print('Sklearn: {}'.format(sklearn.__version__))
print('Matplotlib: {}'.format(matplotlib.__version__))
print('Keras: {}'.format(keras.__version__))

import matplotlib.pyplot as plt 
from pandas.plotting import scatter_matrix

# import the heart disease dataset
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"

# the names will be the names of each column in our pandas DataFrame
names = ['age',
 'sex',
 'cp',
 'trestbps',
 'chol',
 'fbs',
 'restecg',
 'thalach',
 'exang',
 'oldpeak',
 'slope',
 'ca',
 'thal',
 'class']

# read the csv
cleveland = pd.read_csv(url, names=names)

print ('Shape of DataFrame: {}'.format(cleveland.shape))
print (cleveland.loc[1])