import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
# pd.set_option('display.max_rows',None)

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
    #列数量,这里做维度
    dimension = df.shape[1] 
    #行数量,这里做样本数量 
    sampleNum = df.shape[0] 
    #用于存储每个维度平均值的list
    col_mean = []          
    #求每个列的平均值,调用mean_list(list)函数
    for column in colLabels:
        c_mean = mean_list(df[column].values.tolist())
        col_mean.append(round((c_mean),8))
    #开始求相关矩阵
    correlationMatrix = []
    for i in range(dimension):
        valuesRow = []
        for j in range(dimension):
            icol = df.iloc[:,i].tolist()
            jcol = df.iloc[:,j].tolist()
            for k in range(sampleNum):
                icol[k] = round(icol[k]-col_mean[i],7)
                jcol[k] = round(jcol[k]-col_mean[j],7)
            result = 0
            for index in range(sampleNum):
                result+=icol[index]*jcol[index]
            result = round(result/(sampleNum-1),6)
            valuesRow.append(result)
        correlationMatrix.append(valuesRow)

    return correlationMatrix

df = pd.read_csv('./output/Exp01/MergeData.csv')
isnan = df.isnull().all()
dropCol = isnan[isnan.values==True].index.tolist()
df.drop(columns=dropCol,inplace=True)
dfScore = df.iloc[:,5:16]
dfScore = dfScore.T

resultMatrix = corMatrix(dfScore)
nprm = np.array(resultMatrix)
dfresult = pd.DataFrame(data = nprm)
print(dfresult)


