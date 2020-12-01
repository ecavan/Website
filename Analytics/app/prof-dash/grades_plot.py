import numpy as np 
import pandas as pd 
import os

import seaborn as sn
sn.set()

from mock_data import get_mock_data

df = get_mock_data()

def grades_to_plot(df):
    grades_plot =  df[["Midterm", "Quiz 1", "Quiz 2", "Quiz 3"]]
    return grades_plot


grades_plot = grades_to_plot(df)
if __name__ == '__main__':
    grades_plot = grades_to_plot(df)
    #grades_plot.to_excel('/Users/eli/Desktop/Dash/app/data/grades.xlsx')

