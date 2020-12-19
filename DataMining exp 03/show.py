import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_table("./DataMining exp 03/datakmean.txt",sep=',',header=None)
df.columns=['x','y']

# df = pd.read_table("./DataMining exp 03/onestep.txt",sep=',',header=None)
# df.columns=['x','y','cluster']


print(df)


if df.shape[1]==2:
    ax1 = df.plot.scatter(x='x',y='y')
    plt.savefig('./DataMining exp 03/example_x_y.png',bbox_inches='tight')
    plt.show()

if df.shape[1]==3:
    sns.lmplot('x','y',data=df,hue='cluster',fit_reg=False)
    plt.show()