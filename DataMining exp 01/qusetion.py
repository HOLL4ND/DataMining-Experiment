# -*- coding:utf-8 -*-
"""
作者：1806300066-罗乾杰
日期：2020年11月26日
"""
import pandas as pd
import copy


def question_1(data, count):  # 学生中家乡在Beijing的所有课程的平均成绩。
    q1 = []     # 结果
    temp = []   # 暂时保存学生数据
    i = 0
    while i < count:
        if data.loc[i]['City'] == 'Beijing':
            temp.append(data.loc[i]['ID'])
            temp.append(data.loc[i]['Name'])
            aver_Grade = (data.loc[i]['C1'] + data.loc[i]['C2'] + data.loc[i]['C3'] + data.loc[i]['C4'] + data.loc[i]['C5'] +
                          data.loc[i]['C6'] + data.loc[i]['C7'] + data.loc[i]['C8'] + data.loc[i]['C9'] + data.loc[i]['C10']) / 10
            temp.append(aver_Grade)
            a = copy.deepcopy(temp)
            q1.append(a)
            temp.clear()
        i += 1
    print("Beijing的平均成绩")
    for stu in q1:
        print(stu)


def question_3(data, count): # 比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？
    c_Guangzhou = 0
    c_Shanghai = 0
    G_Guangzhou = 0
    G_Shanghai = 0
    i = 0
    while i < count:
        if d.loc[i]['City'] == 'Guangzhou' and d.loc[i]['Gender'] == 'female':
            c_Guangzhou += 1
            G_Guangzhou += d.loc[i]['Constitution']
        if d.loc[i]['City'] == 'Shanghai' and d.loc[i]['Gender'] == 'female':
            c_Shanghai += 1
            G_Shanghai += d.loc[i]['Constitution']
        i += 1
    aver_G = G_Guangzhou / c_Guangzhou
    aver_S = G_Shanghai / c_Shanghai
    print("广州女生平均体能测试成绩:", aver_G)
    print("上海女生平均体能测试成绩:", aver_S)
    if aver_G > aver_S:
        print("广州女生平均体能测试成绩更高。")
    elif aver_S > aver_G:
        print("上海女生平均体能测试成绩更高。")
    else :
        print("广州上海女生平均体能测试成绩一样高。")


if __name__ == '__main__':
    d = pd.read_csv('./output/Exp01/MergeData.csv')
    d = d.fillna(0)
    lenth = len(d)  # 学生人数
    question_1(d, lenth)
    question_3(d, lenth)