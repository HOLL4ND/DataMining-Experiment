# 学习笔记

## Pandas.Dataframe

**dataframe 转 numpy.ndarray** 
Y.values

**dataframe 转置**
dataframe.T

**判断某列是否存在或全为NaN**
dataframe.isnull().any()	#存在NaN
dataframe.isnull().all()	  #全为Nan