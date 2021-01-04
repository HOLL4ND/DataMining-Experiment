# 该文件用于获取学生z-score归一化后的成绩
import pandas as pd

df = pd.read_csv("./output/Exp02/z-score Data.csv")
df.drop(columns=['ID','Name','City','Gender','Height'],inplace=True)
col = df.columns.tolist()
for c in col:
    print(c)
# df.to_csv("./output/Exp02/z-score_scoreOnly.csv",header=True, index=False,float_format='%.8f')
# print(df)