# 数据挖掘-实验

 **To everyone who has forked this repository**
         
 **Thank you**

## 实验内容

:link:[腾讯文档：《机器学习与数据挖掘实验》](https://docs.qq.com/doc/DWXlEWVVZcG5CYWla?groupUin=K2qmpgFfKdRSE7Mz%252FS%252F10A%253D%253D&ADUIN=757685965&ADSESSION=1605947424&ADTAG=CLIENT.QQ.5779_.0&ADPUBNO=27063&_t=1606006564903)

 

 

## 语言支持 

数据分析模块：[pandas](https://pandas.pydata.org/)  |  [Numpy](https://numpy.org/)		

数据可视化模块：：[seaborn](https://seaborn.pydata.org/)  |  [Matplotlib](https://matplotlib.org/)

 

 

## 实验一 《多源数据集成、清洗和统计》

**题目 ：**

​		广州大学某班有同学100人，现要从两个数据源汇总学生数据。第一个数据源在数据库中，第二个数据源在txt文件中，两个数据源课程存在缺失、冗余和不一致性，请用C/C++/Java程序实现对两个数据源的一致性合并以及每个学生样本的数值量化。

 


0.  :white_check_mark: [Code](https://github.com/HOLL4ND/DataMining-Experiment/blob/main/DataMining%20exp%2001/01-00%20mergeData.py) 两个数据源合并后读入内存，并统计：
1.  :white_check_mark: [Code](https://github.com/HOLL4ND/DataMining-Experiment/blob/main/DataMining%20exp%2001/qusetion.py) 学生中家乡在Beijing的所有课程的平均成绩。
2.  :white_check_mark: [Code](https://github.com/HOLL4ND/DataMining-Experiment/blob/main/DataMining%20exp%2001/01-02_04-question.py) 学生家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量。(备注：该处做了修正，课程10数据为空，更改为课程9)
3.  :white_check_mark: [Code](https://github.com/HOLL4ND/DataMining-Experiment/blob/main/DataMining%20exp%2001/qusetion.py) 比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？
4.  :white_check_mark: [Code](https://github.com/HOLL4ND/DataMining-Experiment/blob/main/DataMining%20exp%2001/01-02_04-question.py) 学习成绩和体能测试成绩，两者的相关性是多少？（九门课的成绩分别与体能成绩计算相关性）

 

:warning:  **提示：**

计算部分不能调用库函数；画图/可视化显示可可视化工具或API实现。

 


## 实验二 《数据统计和可视化》

基于**实验一**中清洗后的数据练习统计和视化操作，100个同学（样本），每个同学有11门课程的成绩（11维的向量）；那么构成了一个100x11的数据矩阵。以你擅长的语言C/C++/Java/Python/Matlab，编程计算：

1.  :white_check_mark: [Code](https://github.com/HOLL4ND/DataMining-Experiment/blob/main/DataMining%20exp%2002/02-01%20scatter%20graph.py) 请以课程1成绩为x轴，体能成绩为y轴，画出散点图。
2.  :white_check_mark: [Code](https://github.com/HOLL4ND/DataMining-Experiment/blob/main/DataMining%20exp%2002/02-02%20histogram%20graph.py) 以5分为间隔，画出课程1的成绩直方图。
3.  :white_check_mark: [Code](https://github.com/HOLL4ND/DataMining-Experiment/blob/main/DataMining%20exp%2002/02-03%20z-score.py) 对每门成绩进行z-score归一化，得到归一化的数据矩阵。
4.  :white_check_mark: [Code](https://github.com/HOLL4ND/DataMining-Experiment/blob/main/DataMining%20exp%2002/02-04%20Correlation%20Matrix.py) 计算出100x100的相关矩阵，并可视化出混淆矩阵。（为避免歧义，这里“协相关矩阵”进一步细化更正为100x100的相关矩阵，100为学生样本数目，视实际情况而定）
5.  根据相关矩阵，找到距离每个样本最近的三个样本，得到100x3的矩阵（每一行为对应三个样本的ID）输出到txt文件中，以\t,\n间隔。

 

:warning:  **提示：**

计算部分不能调用库函数；画图/可视化显示可可视化工具或API实现。

 

 


## 实验三  《k-means聚类算法》
:white_check_mark: [Code](https://github.com/HOLL4ND/DataMining-Experiment/blob/main/DataMining%20exp%2003/kmeans.cpp)

用C++实现k-means聚类算法，
1.  对实验二中的z-score归一化的成绩数据进行测试，观察聚类为2类，3类，4类，5类的结果，观察得出什么结论？
2.  由老师给出测试数据，进行测试，并画出可视化出散点图，类中心，类半径，并分析聚为几类合适。



样例数据(x,y)数据对：

| x    | y    |      | x    | y    |      | x    | y    |      | x    | y    |      | x    | y    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 3.45 | 7.08 |      | 6.17 | 5.40 |      | 3.68 | 5.99 |      | 6.24 | 3.06 |      | 3.17 | 6.41 |
| 1.76 | 7.24 |      | 4.20 | 6.46 |      | 2.11 | 4.08 |      | 6.89 | 2.41 |      | 5.97 | 3.62 |
| 4.29 | 9.55 |      | 5.87 | 3.87 |      | 2.58 | 7.10 |      | 5.38 | 2.32 |      | 6.32 | 3.62 |
| 3.35 | 6.65 |      | 5.47 | 2.21 |      | 3.45 | 7.88 |      | 5.13 | 2.73 |      | 7.26 | 4.19 |

![](https://github.com/HOLL4ND/DataMining-Experiment/blob/main/DataMining%20exp%2003/example_x_y.png)



:question:  **问题**  

找到聚类中心后，判断(2,6)是属于哪一类？



:warning:**注意**

除文件读取外，不能使用C++基础库以外的API和库函数。





## 实验四 **《逻辑回归二分类》**

:white_check_mark: [Code](https://github.com/HOLL4ND/DataMining-Experiment/blob/main/DataMining%20exp%2004/LogisticRegression.py)

**题目 ：** 

学习sigmoid函数和逻辑回归算法。将实验三.2中的样例数据用聚类的结果打标签{0，1}，并用逻辑回归模型拟合。

1. 学习并画出sigmoid函数
2. 设计梯度下降算法，实现逻辑回归模型的学习过程。
3. 根据给定数据（实验三.2），用梯度下降算法进行数据拟合，并用学习好的模型对(2,6)分类。



:x:（对2,3实现有难度的同学，可以直接调用[sklearn](https://scikit-learn.org/stable/)中[LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression)进行学习）

:heavy_check_mark:   利用 numpy 实现  



## 小组成员

[林昊蓝](https://github.com/HOLL4ND) HOLL4ND

[罗乾杰](https://github.com/Lier9527) Lier9527

[李志鹏](https://github.com/LIMU-c) LIMU-c

