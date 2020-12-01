import numpy as np 
import pandas as pd 
import os

import seaborn as sn
sn.set()

df = pd.read_excel('/Users/eli/Desktop/Dash/app/data/data.xlsx')


def poly_regress(df, i):
    grades_plot =  df[["Midterm", "Quiz 1", "Quiz 2", "Quiz 3"]]
    marks = df[["Midterm", "Quiz 1", "Quiz 2", "Quiz 3", "Exam", "Overall"]]
    av = marks.agg([np.mean])
    num_stud = 30
    mean = pd.concat([av]*num_stud, ignore_index=True)
    x = [i for i in range(len(grades_plot.columns))]
    x_new = [i for i in range(len(grades_plot.columns)+1)]
    z = [i for i in range(len(mean.columns))]
    p_gr = np.poly1d(np.polyfit(x, grades_plot.iloc[i], len(grades_plot.columns) -2))
    p_av = np.poly1d(np.polyfit(z, mean.iloc[i], len(mean.columns)-1))
    return p_gr
    return p_av 



if __name__ == '__main__':
    #grades_plot = grades_to_plot(df)
    #grades_plot.to_excel('/Users/eli/Desktop/Dash/app/data/grades.xlsx')

