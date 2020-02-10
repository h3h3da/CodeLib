# Python数据处理之幂律拟合

## 设置

主要使用了pandas、matplotlib.pyplot、numpy、sklearn（其实这里最终没用到）以及用于拟合的scipy.optimize的curve_fit。

## 目的

这里的主要目的是对数据进行幂律拟合并进行可视化操作，最后计算一下数据的系数、指数以及R方数据。工作主要有两个，一个是导入Excel表格中的原始数据，生产原始数据散点图；然后对数据进行幂律拟合并对相关参数以及R方进行计算。
这里有一点：对X、Y取双对数后，坐标轴上点可以很好用直线拟合。所以，判定数据是否符合幂律分布，只需要对XY取双对数，判断能否用一个直线很好拟合就行。常见的直线拟合效果评估标准有拟合误差平方和、R平方。因为这里直接对曲线进行的拟合，所以求出的R方数据一直有一些问题，因为计算的TSS和ESS+RSS一直有一些偏差，这里暂时忽略。但对取对数后的数据（可以拟合成线性直线），误差基本可以忽略。
## Reference

[python指数、幂数拟合curve_fit](https://blog.csdn.net/kl28978113/article/details/88818885)
[从excel中读取数据，然后拟合幂律分布](https://blog.csdn.net/zhigang_zhao/article/details/89493488)
[Python数据可视化：幂律分布](https://blog.csdn.net/kevinelstri/article/details/52685934)
[Python 多项式拟合（一元回归）](https://www.cnblogs.com/hzc2012/p/8358302.html)
[用matplotlib画图时，给图像标题、横纵坐标轴的标签、图例显示中文名字](https://blog.csdn.net/qq_25886325/article/details/90600672)
[Python数据可视化:幂律分布实例详解](http://www.cppcns.com/jiaoben/python/291361.html)

