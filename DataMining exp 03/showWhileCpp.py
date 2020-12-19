import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# df = pd.read_table("datakmean.txt",sep=',',header=None)
# df.columns=['x','y']

df = pd.read_table("procedure.txt",sep=',',header=None)
df.columns=['x','y','cluster']
# df = df.tail(28)
df=df.head(20)
cen = pd.read_table("centroid.txt",sep=',',header=None)
# cen = cen.tail(2) 
cen = cen.head(2)
cen.columns=['x','y','cluster','radius']
cenX = cen['x'].tolist()
cenY = cen['y'].tolist()
cenR = cen['radius'].tolist()


if df.shape[1]==2:
    ax1 = df.plot.scatter(x='x',y='y')
    plt.savefig('example_x_y.png',bbox_inches='tight')
    plt.show()

if df.shape[1]==3:
    sns.lmplot('x','y',data=df,hue='cluster',fit_reg=False)
    plt.scatter(cenX[0],cenY[0],color='#3785BC',marker ='x')
    plt.scatter(cenX[1],cenY[1],color='#FFA543',marker ='x')
    plt.axis('equal')
    ax = plt.gca()
    disk1 = plt.Circle((cenX[0],cenY[0]), cenR[0], color='#3785BC', fill=False)
    ax.add_artist(disk1)
    disk2 = plt.Circle((cenX[1],cenY[1]), cenR[1], color='#FFA543', fill=False)
    ax.add_artist(disk2)
    plt.Circle((cenX[0],cenY[0]),cenR[0])
    # plt.scatter(cenX[2],cenY[2],color='#4EAF4E',marker ='x')
    plt.savefig('result.png',bbox_inches='tight')
    plt.show()