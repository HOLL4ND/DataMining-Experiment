# 用于输出老师提供的数据样例
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_table("./DataMining exp 03/datakmean.txt",sep=',',header=None)
df.columns=['x','y']

if df.shape[1]==2:
    ax1 = df.plot.scatter(x='x',y='y')
    plt.savefig('./DataMining exp 03/example_x_y.png',bbox_inches='tight')
    plt.show()
