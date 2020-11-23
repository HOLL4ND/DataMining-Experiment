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

if __name__=='__main__':

    df = pd.read_csv('./resources/Exp01/MergeData.csv')

    #获取课程的列名
    cLabels  = df.columns.values.tolist()[5:15]
    for label in cLabels:
        cList = df[label].tolist()
        cMean = mean_list(cList)
        cSD = SD_list(cList,cMean)
        df[label].fillna(cMean,inplace=True)
        cList = df[label].tolist()
        zList = 0
        for index in range(len(cList)):
            new_num = round((cList[index]-cMean)/cSD,5)
            df.loc[index,label] = new_num
            
    #对每门成绩进行z-scores归一化，得到的数据矩阵:df
    print(df)
    df.to_csv('./resources/Exp01/z-score Data.csv',index=False)