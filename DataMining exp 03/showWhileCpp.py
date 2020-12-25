import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# df = pd.read_table("./sourceData/datakmean.txt",sep=',',header=None)
# df.columns=['x','y']

rawData = pd.read_table('./sourceData/datakmeanAddition.txt',sep=',',header=None)
dataSize = rawData.shape[0]

k=int(input("Enter K:"))

df = pd.read_table("./output/procedure.txt",sep=',',header=None)
df.columns=['x','y','cluster']
df=df.tail(dataSize)

cen = pd.read_table("./output/centroid.txt",sep=',',header=None)
# cen = cen.tail(2) 
cen = cen.tail(k)
cen.columns=['x','y','cluster','radius']

cenX = cen['x'].tolist()
cenY = cen['y'].tolist()
cenR = cen['radius'].tolist()


if df.shape[1]==2:
    ax1 = df.plot.scatter(x='x',y='y')
    plt.savefig('example_x_y.png',bbox_inches='tight')
    plt.show()


colorList = sns.color_palette()
if df.shape[1]==3:
    sns.lmplot('x','y',data=df,hue='cluster',fit_reg=False)
    ax = plt.gca()
    for i in range(k):
        plt.scatter(cenX[i],cenY[i],color=colorList[i],marker ='x')
        plt.scatter(cenX[i],cenY[i],color=colorList[i],marker ='x')
        plt.axis('equal')
        disk1 = plt.Circle((cenX[i],cenY[i]), cenR[i], color=colorList[i], fill=False)
        ax.add_artist(disk1)
        disk2 = plt.Circle((cenX[i],cenY[i]), cenR[i], color=colorList[i], fill=False)
        ax.add_artist(disk2)
    # plt.scatter(cenX[2],cenY[2],color='#4EAF4E',marker ='x')
    plt.savefig('result.png',bbox_inches='tight')
    plt.show()