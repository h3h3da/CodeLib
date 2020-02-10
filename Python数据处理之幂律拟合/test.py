# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from scipy.optimize import curve_fit
from matplotlib.font_manager import FontProperties

# font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)


def func(x, a, b):
    return b * x ** a


def getdata():
    data = pd.read_excel('D:\AFL\Linguistics.xlsx')  # 打开xls文件
    # data = pd.read_excel('D:\AFL\Literature.xlsx')  # 打开xls文件
    x = pd.DataFrame(data, columns=['number'])
    y = pd.DataFrame(data, columns=['frequency'])

    # print(x, y)

    # plt.title("Power-law Distribution Fitting Curve in Linguistics")
    plt.title("Power-law Distribution Fitting Curve in Literature")
    plt.xlabel("Number")
    plt.ylabel("Frequency")

    # 原始数据
    plt.scatter(x, y, color='black', label='Literature')
    # plt.scatter(x, y, color='black', label='Linguistics')

    # 幂律拟合
    x = np.array(x)
    y = np.array(y)

    X = []
    Y = []
    for single_square_feet, single_price_value in zip(x, y):
        X.append(float(single_square_feet))
        Y.append(float(single_price_value))

    popt, pcov = curve_fit(func, X, Y)


    plt.plot(X, func(X, *popt), label='Exponentia', color='red', linewidth=2)

    plt.legend()
    plt.show()

    Ybar = 0.0
    flag = 0
    for i in y:
        Ybar += i[0]
        flag = flag + 1

    print(flag)
    Ybar /= flag

    # TSS
    TSS = 0.0
    for i in y:
        TSS += (i[0] - Ybar) * (i[0] - Ybar)

    print('TSS ' + str(TSS))

    # ESS
    ESS = 0.0
    for i in func(X, *popt):
        ESS += (i - Ybar) * (i - Ybar)

    print('ESS ' + str(ESS))

    # RSS
    RSS = 0.0
    for i,j in zip(y, func(X, *popt)):
        RSS += (i[0] - j) * (i[0] - j)

    print('RSS ' + str(RSS))

    print('ESS + RSS ' + str((ESS + RSS)))

    # R2
    print("function %dx^%f" % (popt[1], popt[0]), "R^2 = %f" % (ESS/TSS))
    x = np.log10(x)
    y = np.log10(y)

    # print(func(X, *popt) == func(X, *popt))

    return x, y

def DataFitAndVisualization(X, Y):
    # 模型数据准备
    X_parameter = []
    Y_parameter = []
    for single_square_feet, single_price_value in zip(X, Y):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append(float(single_price_value))

    # 模型拟合
    regr = linear_model.LinearRegression()

    regr.fit(X_parameter, Y_parameter)
    # 模型结果与得分
    print('Coefficients: \n', regr.coef_, )
    print("Intercept:\n", regr.intercept_)
    # The mean square error
    print("Residual sum of squares: %.8f"
          % np.mean((regr.predict(X_parameter) - Y_parameter) ** 2))  # 残差平方和
    """
          求解 rss ess tss R2 
    """
    Y_h = regr.predict(X_parameter)
    Y = Y_parameter
    X = X_parameter
    rss = np.sum((Y - Y_h) ** 2)
    ess = np.sum((Y_h - np.mean(Y)) ** 2)
    tss = np.sum((Y - np.mean(Y)) ** 2)
    print(rss, ' ', ess, ' ', ess + rss, ' ', tss, ' ', ess / tss)
    ##########
    # 可视化
    plt.title("Log Data")
    plt.scatter(X_parameter, Y_parameter, color='black')
    plt.plot(X_parameter, regr.predict(X_parameter), color='blue', linewidth=3)

    # plt.xticks(())
    # plt.yticks(())
    plt.show()

if __name__ == "__main__":
    x, y = getdata()
    DataFitAndVisualization(x, y)