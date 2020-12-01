import numpy as np 
import pandas as pd 
import os
import random
from pandas import DataFrame

def get_mock_data():
    studentId = []
    num_stud = 30

    for i in range(num_stud):
        studentId.append(random.randint(100000, 999999))
    
    df = DataFrame(studentId,columns=['ID'])
    mid = []
    q1 = []
    q2 =[]
    q3 = []

    for i in range(num_stud):
        mid.append(random.gauss(60, 10))

    for i in range(num_stud):
        q1.append(random.gauss(60, 10))
    
    for i in range(num_stud):
        q2.append(random.gauss(70, 5))
    
    for i in range(num_stud):
        q3.append(random.gauss(65, 10))
    
    df.insert(1, "Midterm", mid)
    df.insert(2, "Quiz 1", q1)
    df.insert(3, "Quiz 2", q2)
    df.insert(4, "Quiz 3", q3)

    Qb = pd.read_csv('2018.csv')
    names = Qb['Player'][0:30]

    df.insert(5, "Names", names)


    exam = []
    for i in range(num_stud):
        exam.append(random.gauss(55, 10))
    
    df.insert(6, "Exam", exam)

    Q_avg = []

    for i in range(0, num_stud):
        avg = (df.loc[i][2] + df.loc[i][3] + df.loc[i][4])*0.33
        Q_avg.append(avg)
    
    df.insert(7, "Quiz average", Q_avg)

    overall = []
    for i in range(0,num_stud):
        if pd.isnull(df.loc[i][1]) == True:
            grade2 = (df.loc[i][6] + df.loc[i][7])*0.5
            overall.append(grade2)
        elif pd.isnull(df.loc[i][6]) == True:
            grade3 = df.loc[i][1]*0.6 + (df.loc[i][7])*0.4
            overall.append(grade3)    
        else:
            grade = df.loc[i][1]*0.35 + (df.loc[i][7])*0.25 + (df.loc[i][6])*0.4
            overall.append(grade)
                
    df.insert(8, "Overall", overall)


    rate = []
    for i in range(num_stud):
        rate.append(random.randint(0, 10))
    
    df.insert(9, "Student Rating", rate)


    com = []

    for i in range(num_stud):
        com.append(random.gauss(60, 10))
    
    df.insert(9, "Comments", com)

    return df