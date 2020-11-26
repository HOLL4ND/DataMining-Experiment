'''
软件183
李志鹏
'''

import pandas as pd
import numpy as np

#学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量---问题二
def Num_boy(df):
    num = 0
    row = df.shape[0] - 1
    for i in range(row):
        if(df['City'][i] == 'Guangzhou' and df['C1'][i] >= 80 and df['C9'][i] >= 90 and df['Gender'][i] == ' male '):
            num += 1
       
    print("The number of male students:" ,num)

#----------------------------------------------------------------------------------------

#学习成绩和体能测试成绩，两者的相关性是多少？-----问题四

#平均值
def mean(df , title):
    sum = 0
    row = df.shape[0] 
    for i in range(row):
        sum += df[title][i]
    mean_sum = sum / row
    return mean_sum

#标准差
def std(df , title ):
    std_x = 0    #协方差
    std_b = 0    #标准差
    sum_xi2 = 0
    sum_xi = 0
    row = df.shape[0] 
    for i in range(row):
        sum_xi2 += df[title][i] * df[title][i]

    for i in range(row):
        sum_xi += df[title][i] 

    std_x = (sum_xi2 - sum_xi * sum_xi / (row + 1)) / row  #row为0-105 ，则实际函数应为 row + 1 = 126 。因此，n = row + 1
    std_b = std_x ** 0.5
    return std_b


#A'
def ak(df , title):
    row = df.shape[0] 
    list_a = {}
    mean_sum = mean(df,title)
    std_sum = std(df , title)
    for i in range(row):
        list_a[i] = (df[title][i] - mean_sum) / std_sum

    return list_a


#B'
def bk(df):
    row = df.shape[0] 
    list_b = {}
    mean_sum = mean(df,'Constitution')
    std_sum = std(df ,'Constitution' )
    for i in range(row):
        list_b[i] = (df['Constitution'][i] - mean_sum) / std_sum

    return list_b


#问题四
def Correlation(df , title):
    correlation_sum = 0
    list_a = ak(df,title)
    list_b = bk(df)
    row = df.shape[0]
    for i in range(row):
        correlation_sum += list_a[i] * list_b[i]
    
    print("The correlation coefficient between course '%s' and course 'Constitution' is:%f"  % (title, correlation_sum))

if __name__ == '__main__':
    df = pd.read_csv('./output/Exp01/MergeData.csv')

    #问题二
    Num_boy(df)

    #问题四
    Correlation(df , 'C1')
    Correlation(df , 'C2')
    Correlation(df , 'C3')
    Correlation(df , 'C4')
    Correlation(df , 'C5')
    Correlation(df , 'C6')
    Correlation(df , 'C7')
    Correlation(df , 'C8')
    Correlation(df , 'C9')

