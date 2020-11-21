from numpy.core.defchararray import index
import pandas as pd
import numpy as np
pd.set_option('display.max_rows',None)

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
    else:
        return consti

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


converters={'Gender':lambda x:gen(x),'Height':lambda x: height(x),'Constitution':lambda x:conChange(x)}

#-----------------df1----------------------
df1 = pd.read_table('./DM exm/resources/01dataSource.txt',sep=',',converters=converters)

tpToPer(df1)

df1 = df1.drop_duplicates(keep='first')               #去除完全相同的
df1 = df1.drop_duplicates(subset=['ID'],keep='first') #暴力去重，ID重复则只保留第一个
df1.sort_values('ID',inplace=True)
df1 = df1.reset_index(drop=True)                #去除后重设打乱的index

# print(df1.shape)


#-----------------df2----------------------
df2 = pd.read_excel('./DM exm/resources/01dataSource.xlsx',converters=converters)

def compID(id):
    x=int(id)
    return 202000+x

df2['ID']=df2['ID'].apply(compID)

tpToPer(df2)

df2 = df2.drop_duplicates(keep='first')               #去除完全相同的
df2 = df2.drop_duplicates(subset=['ID'],keep='first') #暴力去重，ID重复则只保留第一个
df2.sort_values('ID',inplace=True)
df2 = df2.reset_index(drop=True)                      #去除后重设打乱的index
# print(df2.shape)



#------------------df----------------------
df=pd.concat([df1,df2],ignore_index=True)
df.sort_values('ID',inplace=True)

df = df.drop_duplicates(keep='first')           #去除完全相同的行

df = df.reset_index(drop=True)
dup = df.duplicated(subset=['ID'])
dupIndex = dup[dup.values==True].index.tolist() #获取‘ID’冗余（第二次出现）的行

#用于判断位于[row,col]的值是否为Nan (pd.isna(df.iloc[row,col])) 
#定位元素(df.iloc[row, col])

# print(dupIndex)

for row in dupIndex:
    col=df.shape[1] # 16
    for col in range(col):
        if pd.isna(df.iloc[row-1,col]):
            df.iloc[row-1,col]=df.iloc[row,col]

df = df.drop_duplicates(subset=['ID'],keep='first')           #去除ID相同的行
df = df.reset_index(drop=True)

# print(df)
df.to_excel('output.xlsx',index=False)
print("done")