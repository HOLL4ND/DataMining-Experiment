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

def SD_list(list,mean):
    '''
    返回列表的标准差，计算时跳过空缺值
    '''   
    #均值为nan直接返回nan
    if math.isnan(mean):
        return float('nan')
    
    sumX2=float(0)
    n = float(len(list))
    for num in list:
        #跳过空缺值
        if math.isnan(num):
            n-=1
            continue
        sumX2 += pow(num,2)
    
    SD_list = math.sqrt(sumX2/n - pow(mean,2))

    return SD_list

def z_score(df,colList=None):
    #如果没有给出列名则对整个dataframe 作z-score归一化
    if colList is None:
        
        return
    for label in colList:
        cList = df[label].tolist()
        cMean = mean_list(cList)
        cSD = SD_list(cList,cMean)
        df[label].fillna(cMean,inplace=True)
        cList = df[label].tolist()
        for index in range(len(cList)):
            new_num = round((cList[index]-cMean)/cSD,5)
            df.loc[index,label] = new_num


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

if __name__ == '__main__':
    
    #读取合并后的数据
    df = pd.read_csv('./output/Exp01/MergeData.csv')
    
    #去除完全空缺的列
    isnan = df.isnull().all()
    dropCol = isnan[isnan.values==True].index.tolist()
    df.drop(columns=dropCol,inplace=True)

    #提取数值数据
    dfScore = df.iloc[:,5:16]

    #进行矩阵的转置
    dfScore = dfScore.T

    z_score(df)
    resultMatrix = corMatrix(dfScore)
    nprm = np.array(resultMatrix)
    dfresult = pd.DataFrame(data = nprm)
    print(dfresult)


