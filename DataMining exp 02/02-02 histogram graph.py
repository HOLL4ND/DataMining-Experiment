import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./output/Exp01/MergeData.csv')

#取出C1列
c1 = df['C1'].values

# 对取出的ndarray进行排序
c1Sorted = np.sort(c1)

#找到最小值 最大值
c1min = c1Sorted[0]
c1max = c1Sorted[-1]

#划分
start = 10*(c1min//10)
end = 10*(c1max//10) + 1
bins = np.arange(start,end,5)

#作图
(n, bins, patches) = plt.hist(c1Sorted,bins,alpha = 0.6)
x = np.arange(start+5/2,end-5/2,5)

#给hist图添加数值
for i, v in enumerate(n):
    plt.text(x[i],v,str(int(v)),horizontalalignment='center')

#给图加标题,中文需添加第4,5行代码
plt.title("C1分数区间统计")

#保存图
plt.savefig('./DataMining exp 02/02-02.png',bbox_inches='tight')

plt.show()

