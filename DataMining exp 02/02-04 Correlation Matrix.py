import pandas as pd
import math
import matplotlib.pyplot as plt
pd.set_option('display.max_rows',None)

def mean_list(list)->float:
    '''
    返回列表的平均值，计算时跳过空缺值
    '''
    sum=float(0)
    n = float(len(list))
    for num in list:
        #跳过空缺值
        if math.isnan(num):
            n-=1
            continue
        sum += num
    #list中没有有效值
    if n == 0:
        return float('nan')
    mean = sum/n
    return mean

def corMatrix(df):
    colLabels  = df.columns.values.tolist()
    dim = len(colLabels)
    print(dim)
    col_mean = []
    for column in colLabels:
        c_mean = mean_list(df[column].values.tolist())
        col_mean.append(c_mean)
    print(col_mean)


df = pd.read_csv('./resources/Exp01/MergeData.csv')
isnan = df.isnull().all()
dropCol = isnan[isnan.values==True].index.tolist()
dfScore = df.iloc[:,5:16]
dfScore.drop(columns=dropCol,inplace=True)

dfScore = dfScore.T
dfScore.to_csv('./output/Exp02/dfT.csv',index=False)

corMatrix(dfScore)

dim = len(dfScore.columns.values)