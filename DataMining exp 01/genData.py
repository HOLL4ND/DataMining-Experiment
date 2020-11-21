
# * 该程序用于向mysql中生成100条学生数据

from random import randint
from pypinyin import pinyin, lazy_pinyin, Style
import pymysql.cursors
import random


txtpath ="./DM exm/resources/CFname.txt"
familyName = [] # 姓氏拼音列表
city=['Beijing','Guangzhou','Shenzhen','Shanghai']
constitution=['bad','general','good','excellent']
gender=['boy','girl']

student = []

f=open(txtpath,encoding='utf-8')
line = f.readline().replace('\n','')
pyName = lazy_pinyin(line)[0].capitalize()
familyName.append(pyName)
while line:
    line = f.readline().replace('\n','')
    if len(line)!=0:
        pyName = lazy_pinyin(line)[0].capitalize()
        familyName.append(pyName)

for i in range(1,101):
    aStu=[]
    aStu.append(int(i))
    aStu.append(familyName[random.randint(0,149)])
    aStu.append(city[random.randint(0,3)])
    aStu.append(gender[random.randint(0,1)])
    aStu.append(float(random.randint(165,185)))
    for j in range(5):
        aStu.append(float(random.randint(65,95)))
    for j in range(5):
        aStu.append(float(random.randint(7,10)))
    aStu.append(constitution[random.randint(0,3)])

    student.append(tuple(aStu))

for stu in student:
    print(stu)
# #*Student list done


db = pymysql.connect(host="localhost",user="root",db="studenttest")
cursor = db.cursor()#获取游标

cursor.executemany("INSERT INTO student (ID,Name,City,Gender,Height,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,Constitution) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )",student)

# sql="INSERT INTO student (ID,Name,City,Gender,Height,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,Constitution) VALUES (%d,%s,%s,%s,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%s )"%student[0]
# sql="select * from student"
# cursor.execute(sql) 
# data=cursor.fetchall()
# print(data)

db.commit()

# pyin = lazy_pinyin(nm).capitalize()
# print(pyin)