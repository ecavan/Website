import numpy as np 
import pandas as pd 
import os

import seaborn as sn
sn.set()

from mock_data import get_mock_data

df = get_mock_data()

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from numpy import random, float

from grades_plot import grades_to_plot 


grades_plot = grades_to_plot(df)

num_stud = 30

def mid(grades_plot):

    grades_plot2 = grades_plot.copy(deep=False)
    mid = grades_plot.loc[:, grades_plot.columns == 'Midterm']
    return mid

    

def q_avg(grades_plot):   
    
    Q_avg = []

    for i in range(0, num_stud):
        avg = np.mean(grades_plot.iloc[i])
        Q_avg.append(avg)
    

    return Q_avg


def model(mid):
    model = KMeans(n_clusters=4)
    return model.fit(scale(mid))

if __name__ == '__main__':
    mid = mid(grades_plot)
    model = model(mid)
    print(model)