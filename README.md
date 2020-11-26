[TOC]

# 数据挖掘-实验

## 实验内容

:link:[腾讯文档：《机器学习与数据挖掘实验》](https://docs.qq.com/doc/DWXlEWVVZcG5CYWla?groupUin=K2qmpgFfKdRSE7Mz%252FS%252F10A%253D%253D&ADUIN=757685965&ADSESSION=1605947424&ADTAG=CLIENT.QQ.5779_.0&ADPUBNO=27063&_t=1606006564903)

## 实验一 《多源数据集成、清洗和统计》

0.  :white_check_mark: 两个数据源合并后读入内存，并统计：
1.  :white_check_mark: 学生中家乡在Beijing的所有课程的平均成绩。
2.  :white_check_mark: 学生家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量。(备注：该处做了修正，课程10数据为空，更改为课程9)
3.  :white_check_mark: 比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？
4.  :white_check_mark: 学习成绩和体能测试成绩，两者的相关性是多少？（九门课的成绩分别与体能成绩计算相关性）



## 实验二 《数据统计和可视化》

基于**实验一**中清洗后的数据练习统计和视化操作，100个同学（样本），每个同学有11门课程的成绩（11维的向量）；那么构成了一个100x11的数据矩阵。以你擅长的语言C/C++/Java/Python/Matlab，编程计算：

1.  :white_check_mark: 请以课程1成绩为x轴，体能成绩为y轴，画出散点图。
2.  :white_check_mark: 以5分为间隔，画出课程1的成绩直方图。
3.  :white_check_mark: 对每门成绩进行z-score归一化，得到归一化的数据矩阵。
4.  :soon: 计算出100x100的相关矩阵，并可视化出混淆矩阵。（为避免歧义，这里“协相关矩阵”进一步细化更正为100x100的相关矩阵，100为学生样本数目，视实际情况而定）
5. 根据相关矩阵，找到距离每个样本最近的三个样本，得到100x3的矩阵（每一行为对应三个样本的ID）输出到txt文件中，以\t,\n间隔。



## 小组成员

[林昊蓝](https://github.com/HOLL4ND)	HOLL4ND

[罗乾杰](https://github.com/Lier9527) Lier9527

[李志鹏](https://github.com/LIMU-c) LIMU-c

