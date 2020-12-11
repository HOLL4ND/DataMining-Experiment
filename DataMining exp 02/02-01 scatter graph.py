import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./output/Exp01/MergeData.csv')

x = df['C1'].values
y = df['Constitution'].values
plt.scatter(x,y)
plt.xlabel('C1 Score')
plt.ylabel('Constitution')
plt.savefig('./DataMining exp 02/02-01.png',bbox_inches='tight')
plt.show()

