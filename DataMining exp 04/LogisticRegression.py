# -*- coding:utf-8 -*-
"""
日期：2020年12月21日
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import numpy.random
import time
n = 20  # 样本数量


def sigmoid(x):     # sigmoid函数
    return 1/(1+np.exp(-x))


def model(X, theta):     # 预测函数     θ0+θ1*x1 + θ2*x2
    return sigmoid(np.dot(X, theta.T))  # 矩阵乘法


def cost(X, Y, theta):  # 损失函数      对数似然函数取负号
    left = np.multiply(-Y, np.log(model(X, theta)))     # 对应位置相乘
    right = np.multiply(1-Y, np.log(1-model(X, theta)))  # 对应位置相乘
    return np.sum(left-right)/(len(X))  # 平均损失值


def gradient(X, Y, theta):    # 计算梯度    对θj求偏导
    grad = np.zeros(theta.shape)    # 初始化grad数组
    error = (model(X, theta)-Y).ravel()     # 转化为一维数组
    for j in range(len(theta.ravel())):
        term = np.multiply(error, X[:, j])
        grad[0, j] = np.sum(term) / len(X)
    return grad


def stopCriterion(value, threshold):
    return value > threshold


def shuffleData(data):      # 打乱数据
    np.random.shuffle(data)
    cols = data.shape[1]    # 列数
    X = data[:, 0:cols-1]
    Y = data[:, cols-1:]
    return X, Y


def descent(data, theta, batchSize, thresh, alpha):       # 梯度下降函数
    init_time = time.time()
    i = 0   # 记录迭代次数
    k = 0   # batch
    X, Y = shuffleData(data)    # 洗数据
    grad = np.zeros(theta.shape)
    costs = [cost(X, Y, theta)]
    while True:
        grad = gradient(X[:batchSize], Y[:batchSize], theta)    # 计算梯度
        X, Y = shuffleData(data)    # 重新洗牌
        theta = theta - alpha*grad  # 参数更新
        costs.append(cost(X, Y, theta))   # 计算新的损失
        i += 1  # 迭代次数加1
        if stopCriterion(i, thresh):
            break
    return theta, i-1, costs, grad, time.time()-init_time


def runExpe(data, theta, batchSize, thresh, alpha):   # 逻辑回归
    theta, iter, costs, grad, dur = descent(data, theta, batchSize, thresh, alpha)    # 梯度下降
    # 输出图像
    name = "Original"
    name += "data - learning rate: {} -".format(alpha)  # 学习率
    strDescType = "Gradient "    # 全量梯度下降
    name += strDescType + "desent - Stop "  # 到达一定迭代次数停止
    strStop = "{}iterations".format(thresh)    # 迭代次数
    name += strStop

    print(name, "\nTheta:", theta, "  - Iter:", iter, "- Last cost:", costs[-1], "- Duration:", dur)

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(np.arange(len(costs)), costs, 'r')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Cost')
    ax.set_title(name.upper() + ' - Error vs. Iteration')
    plt.show()
    return theta


def predict(X, theta):
    return [1 if x >= 0.5 else 0 for x in model(X, theta)]


def bin(x):
    tag = float(x)
    if tag == 2:
        return 1
    elif tag == 1:
        return 0


converter = {'class': lambda x: bin(x)}
pddata = pd.read_csv('./DataMining exp 03/output/clustering result k 2.txt',dtype=float,converters=converter)
pddata.columns = ['x', 'y', 'z']
positive = pddata[pddata['z'] == 1]
negative = pddata[pddata['z'] == 0]
fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(positive['x'], positive['y'], s=30, c='b', marker='o', label='1')
ax.scatter(negative['x'], negative['y'], s=30, c='r', marker='x', label='0')
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')

# 逻辑回归
pddata.insert(0, 'Ones', 1)  # 添加1列全为1
orig_data = pddata.values   # 转为列表
cols = orig_data.shape[1]   # 列数
X = orig_data[:, 0:cols-1]
Y = orig_data[:, cols-1:cols]
theta = np.zeros([1, 3])    # 初始化θ
theta = runExpe(orig_data, theta, n, thresh=5000, alpha=0.001)  # 逻辑回归取得合适的theta值

# 画出sigmoid函数图像
x = np.dot(X, theta.T)
y = sigmoid(np.dot(X, theta.T))
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.scatter(x, y, s=30, c='b', marker='o')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
plt.show()

# 预测（6,2）的类别
test = [1., 6, 2]   # 预测（6,2）的类别    0 or 1
prediction1 = predict(X, theta)
prediction2 = predict(test, theta)  #
flag = 0
for i in range(len(Y)):
    if prediction1[i] == Y[i]:
        flag += 1
ac = flag/len(Y)    # 正确率
print("\n正确率", ac)
print("(6,2)的预测结果为", prediction2[0])



