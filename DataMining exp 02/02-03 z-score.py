import pandas as pd
import math
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
        cList = df.columns.values.tolist()
        for label in cList:
            cList = df[label].tolist()
            cMean = mean_list(cList)
            cSD = SD_list(cList,cMean)
            df[label].fillna(cMean,inplace=True)
            cList = df[label].tolist()
            for index in range(len(cList)):
                new_num = round((cList[index]-cMean)/cSD,5)
                df.loc[index,label] = new_num
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


if __name__=='__main__':

    #获取合并后的数据
    df = pd.read_csv('./output/Exp01/MergeData.csv')

    #去除完全空缺的列
    isnan = df.isnull().all()
    dropCol = isnan[isnan.values==True].index.tolist()
    df.drop(columns=dropCol,inplace=True)

    #获取课程的列名
    cLabels  = df.columns.values.tolist()[5:16]

    #对给dataframe中给定列名进行z-score归一化
    z_score(df,cLabels)

    #输出实验结果
    # print(df)

    dfScore = df.iloc[:,5:16]

    #进行矩阵的转置
    dfScore = dfScore.T
    # colList = dfScore.columns.values.tolist()

    print(dfScore)


    #保存实验结果
    # df.to_csv('./output/Exp02/z-score Data.csv',index=False)