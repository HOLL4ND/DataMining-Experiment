# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-10,10,0.1)
y = 1./(1.+np.exp(-x))

plt.plot(x, y)
plt.show()