from numpy.core.defchararray import index
import pandas as pd
import numpy as np
import math
pd.set_option('display.max_rows',None)

#性别统一使用 male 和 female
def gen(gender):
    if gender=='boy':
        return 'male'
    elif gender == 'girl':
        return 'female'
    else:
        return gender

#身高统一使用单位：米
def height(height):
    h = float(height)
    if h>10:
        h=h/100.0
        return h
    else:
        return h

#体侧成绩转百分制
def conChange(consti):
    if consti == 'excellent':
        return 90
    elif consti == 'good':
        return 80
    elif consti == 'general':
        return 70
    elif consti == 'bad':
        return 60
    elif consti=='':
        return np.NaN

def TenTimes(score):
    if score=='':
        return score
    s=float(score)*10
    return s

#十分制成绩转为百分制
def tpToPer(df):
    df['C6']=df['C6'].apply(TenTimes)
    df['C7']=df['C7'].apply(TenTimes)
    df['C8']=df['C8'].apply(TenTimes)
    df['C9']=df['C9'].apply(TenTimes)
    df['C10']=df['C10'].apply(TenTimes)

#合并处理函数
def dupMerge(dataframe):
    '''
    合并处理函数,仅保留重复的第一个值,如果行中有空缺则向重复行寻找
    '''
    df=dataframe

    #根据ID排序
    df.sort_values('ID',inplace=True)   

    #去除完全重复的行
    df = df.drop_duplicates(keep='first')               #去除完全相同的   

    #重设index
    df = df.reset_index(drop=True)      

    #定位'ID'重复的位置，位置存入 dupStartList=>List
    idcol = df['ID']
    oneDup = idcol.drop_duplicates(keep='first')
    notDup = idcol.drop_duplicates(keep=False)
    dupStart=oneDup.append(notDup).drop_duplicates(keep=False)

    #所有重复数据的起始处保存为列表List
    dupStartList = dupStart.index.tolist()
    
    #取列数 
    col = df.shape[1]  

    #处理'ID'重复的数据
    for row in dupStartList:
        dupStart = opFlag = row
        dupEnd = row
        #找到重复区间，dupEnd为重复结束index
        while df.iloc[dupEnd,0] == df.iloc[dupEnd+1,0]:
            dupEnd=dupEnd+1
        #如果出现空值，则向下查找非空值
        for c in range(col):
            if pd.isna(df.iloc[dupStart,c]):
                while dupEnd - opFlag > 0:
                    opFlag = opFlag + 1
                    if not pd.isna(df.iloc[opFlag,c]):
                        df.iloc[dupStart,c] = int(df.iloc[opFlag,c])
                        break

    #处理结束后，去除其他重复行
    df = df.drop_duplicates(subset=['ID'],keep='first')

    #重设index
    df = df.reset_index(drop=True)      

    return df

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

def fillNaN(df):
    cLabels  = df.columns.values.tolist()[5:16]
    for label in cLabels:
        cList = df[label].tolist()
        cMean = mean_list(cList)
        if math.isnan(cMean):
            continue
        df[label].fillna(cMean,inplace=True)


if __name__ == '__main__':

    converters={'Gender':lambda x:gen(x),'Height':lambda x: height(x),'Constitution':lambda x:conChange(x)}


    #-----------------df1----------------------
    df1 = pd.read_table('./resources/Exp01/01dataSourcecp.txt',sep=',',converters=converters)

    tpToPer(df1)

    df1 = dupMerge(df1)

    #-----------------df2----------------------
    df2 = pd.read_excel('./resources/Exp01/01dataSource.xlsx',converters=converters)

    #学生ID处理函数
    def compID(id):
        x=int(id)
        return 202000+x

    df2['ID']=df2['ID'].apply(compID)

    tpToPer(df2)

    df2 = dupMerge(df2)

    #------------------df----------------------
    #合并两表
    df = pd.concat([df1,df2],ignore_index=True)
    df = dupMerge(df)

    #将空缺处填上该列均值
    fillNaN(df)

    #最终合并的dataframe=>'df'
    print(df) 

    #将结果保存到csv中
    df.to_csv('./resources/Exp01/MergeData.csv',index=False)

    print("done")

