# 实验一 《多源数据集成、清洗和统计》

## 数据源

- 数据库表：ID (int), 姓名(string), 家乡(string:限定为Beijing / Guangzhou / Shenzhen / Shanghai), 性别（string:boy/girl）、身高（float:单位是cm)）、课程1成绩（float）、课程2成绩（float）、...、课程10成绩(float)、体能测试成绩（string：bad/general/good/excellent）；其中课程1-课程5为百分制，课程6-课程10为十分制。

- txt文件：ID(string：6位学号)，性别（string:male/female）、身高（string:单位是m)）、课程1成绩（string）、课程2成绩（string）、...、课程10成绩(string)、体能测试成绩（string：差/一般/良好/优秀）；其中课程1-课程5为百分制，课程6-课程10为十分制。



**数据库中Stu表数据**

:link:  [student data.csv](https://github.com/HOLL4ND/DataMining-Experiment/blob/main/resources/Exp01/01dataSource.csv)

| ID   | Name | City     | Gender | Height | C1   | ...  | C10  | Constitution |
| ---- | ---- | -------- | ------ | ------ | ---- | ---- | ---- | ------------ |
| 1    | Sun  | Beijing  | boy    | 160    | 87   |      | 9    | good         |
| 2    | Zhu  | Shenzhen | girl   | 177    | 66   |      | 8    | excellent    |
| ...  | ...  | ...      | ...    | ...    | ...  | ...  | ...  | ...          |

**student.txt中**

:link:  [student data.txt](https://github.com/HOLL4ND/DataMining-Experiment/blob/main/resources/Exp01/01dataSource.txt)

ID,Name,City,Gender,Height,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,Constitution
202001,Marks,Shenzhen,male,1.66,77,100,84,71,91,6,7,6,8,,general
202002,Wayne,Shenzhen,female,1.59,77,78,89,59,93,10,6,5,9,,good
202003,Bonnie,Guangzhou,girl,1.57,80,81,81,54,91,9,6,7,8,,good





## 实验内容

:white_check_mark: [Code](https://github.com/HOLL4ND/DataMining-Experiment/blob/main/DataMining%20exp%2001/01-00%20mergeData.py) 两个数据源合并后读入内存，并统计