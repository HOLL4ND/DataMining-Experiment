from numpy.core.defchararray import index
import pandas as pd
import numpy as np
# pd.set_option('display.max_rows',None)

def gen(gender):
    if gender=='boy':
        return 'male'
    elif gender == 'girl':
        return 'female'
    else:
        return gender

def height(height):
    h = float(height)
    if h>10:
        h=h/100.0
        return h
    else:
        return h

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

def tpToPer(df):
    df['C6']=df['C6'].apply(TenTimes)
    df['C7']=df['C7'].apply(TenTimes)
    df['C8']=df['C8'].apply(TenTimes)
    df['C9']=df['C9'].apply(TenTimes)
    df['C10']=df['C10'].apply(TenTimes)


def dupMerge(dataframe):

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

converters={'Gender':lambda x:gen(x),'Height':lambda x: height(x),'Constitution':lambda x:conChange(x)}


#-----------------df1----------------------
df1 = pd.read_table('./resources/Exp01/01dataSourcecp.txt',sep=',',converters=converters)

tpToPer(df1)

df1 = dupMerge(df1)

#-----------------df2----------------------
df2 = pd.read_excel('./resources/Exp01/01dataSource.xlsx',converters=converters)

def compID(id):
    x=int(id)
    return 202000+x

df2['ID']=df2['ID'].apply(compID)

tpToPer(df2)

df2 = dupMerge(df2)


#------------------df----------------------
df = pd.concat([df1,df2],ignore_index=True)
df = dupMerge(df)

# print(df) #最终合并的dataframe

df.to_csv('./resources/Exp01/MergeData.csv',index=False)

print("done")

