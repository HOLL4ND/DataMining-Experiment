import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table("./DataMining exp 03/eee.txt",sep=',')
print(df)

ax1 = df.plot.scatter(x='x',y='y')
plt.savefig('./DataMining exp 03/example_x_y.png',bbox_inches='tight')

plt.show()