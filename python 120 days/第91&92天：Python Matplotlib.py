import matplotlib.pyplot as plt
import numpy as np

# 指定一个画板
fig = plt.figure()
# 指定画板后指定轴
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
plt.show()

# plot(xdata, ydata, format)
# xdata: 所有点的x坐标，如果不传默认是[0:]
# ydata: 所有点的y坐标
# format: 绘制的格式，默认是'b-'。比如'b-+': 分别代表颜色、线形和标记。
plt.plot([1, 2], [1, 2], 'r--+')
plt.show()

x = (1, 3, 5, 9, 13)
y = (2, 5, 9, 12, 28)
# 调用绘制方法
# 设置线条属性
# linewidth属性设置线条的宽度
plt.plot(x, y, 'b-+')
plt.show()

# 折线图
# 绘制x轴数据
x = np.arange(2, 15)
y = 3 * x + 6
# 给图形设置标题
plt.title('line char')
# 设置x轴和y轴的属性名
plt.xlabel("x axis")
plt.ylabel("y axis")
# 绘制图形
plt.plot(x, y)
# 显示图形
plt.show()

x = np.arange(2, 15)
y = 2 * x + 6
plt.title("scatter chart")
plt.xlabel("x axis")
plt.ylabel("y axis")
# 设置图形样式和颜色
plt.plot(x, y, "oc")
plt.show()

# 绘制一个倒三角图形
x = np.arange(2, 15)
y = 2 * x + 6
plt.title("triangle_scatter chart")
plt.xlabel("x axis")
plt.ylabel("y axis")
# 设置图形样式和颜色
plt.plot(x, y, "^c")
plt.show()

# 正余弦波形图
print(np.pi)
# 绘制x轴，从0开始
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
# 设置标题
plt.title("sine wave from")
# 绘制图形点
plt.plot(x, y, 'y')
plt.show()

# 余弦波形图
# 绘制x轴，从0开始
x = np.arange(0, 4 * np.pi, 0.1)
y = np.cos(x)
# 设置标题
plt.title("cosine wave form")
# 绘制图形点
plt.plot(x, y, 'm')
plt.show()

# 正余弦波形图
# 在matplotlib中，一个Figure对象可以包含多个子图(Axes)，可以使用subplot()快速绘制：
# subplot(numRows, numCols, plotNum)
# 图表的整个绘图区域被分成 numRows 行和 numCols 列
# plotNum 参数指定创建的 Axes 对象所在的区域
plt.subplot(2, 2, 1)
plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2, 2, 1)', ha='center', va='center', size=20, alpha=.5)
plt.subplot(2, 2, 2)
plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2, 2, 2)', ha='center', va='center', size=20, alpha=.5)
plt.subplot(2, 2, 3)
plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2, 2, 3)', ha='center', va='center', size=20, alpha=.5)
plt.subplot(2, 2, 4)
plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2, 2, 4)', ha='center', va='center', size=20, alpha=.5)
# 0.5 0.5 为文本的边距
plt.show()

# 正余弦函数波形图subplot
# 计算正弦和余弦曲线上的点的x和y坐标
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# 建立subplot网络格，高为2，宽为1
# 激活第一个subplot
plt.subplot(2, 1, 1)
# 绘制第一个图像
plt.plot(x, y_sin)
plt.title('Sine')
# 激活第二个subplot，并绘制第二个图像
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')
plt.show()

# 直方图
# 设置x的x轴和y轴数值
x = [5, 8, 10]
y = [12, 16, 6]
# 设置x2的x轴和y轴数值
x2 = [6, 9, 11]
y2 = [6, 15, 7]
# 使用bar()函数设置条形图的颜色和对齐方式
plt.bar(x, y, color='y', align='center')
plt.bar(x2, y2, color='c', align='center')
# 设置标题
plt.title('Bar chart')
# 设置x轴和y轴的属性名
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()

# Matplotlib 结合 NumPy 使用
# NumPy 中的直方统计函图：histogram
# histogram(a,bins=10,range=None,weights=None,density=False)
# 参数说明：
# a 待统计数据的数组
# bins 指定统计的区间个数
# range 一个长度为2的元组，表示统计范围的最小值和最大值，默认值None，表示范围由数据的范围决定
# weights 为数组的每个指定了权值，histogram()会对区间中数组所对应的权值进行求和
# density 为True时，返回每个区间的概率密度；为False时，返回每个区间中元素的个数
# 函数说明
# numpy.histogram() 函数是数据的频率分布的图形表示。水平尺寸相等的矩形对应于类间隔，称为 bin，变量 height 对应于频率。
# numpy.histogram() 函数将输入数组和 bin 作为两个参数。bin 数组中的连续元素用作每个 bin 的边界。

# 赋值数组a
a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
# 调用函数
np.histogram(a, bins=[0, 20, 40, 60, 80, 100])
hist, bins = np.histogram(a, bins=[0, 20, 40, 60, 80, 100])
# 输出值
print(hist)
print(bins)
# plt()函数使用：
a = np.array([22, 87, 43, 56, 73, 55, 11, 20, 51, 5, 79, 27, 100])
# plt()函数将数据变为直方图
plt.hist(a, bins=[0, 20, 40, 60, 80, 100])
plt.title("histogram")
plt.show()

# 曲线图
n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)
plt.plot(X, Y + 1, color='blue', alpha=1.00)
plt.plot(X, Y - 1, color='blue', alpha=1.00)
plt.title('curve_chart1')
plt.show()

# 升级版的曲线图
n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)
plt.plot(X, Y + 1, color='blue', alpha=1.00)
plt.fill_between(X, 1, Y + 1, color='blue', alpha=.25)
plt.plot(X, Y - 1, color='blue', alpha=1.00)
# 设置线条颜色和填充颜色区域
plt.fill_between(X, -1, Y - 1, (Y - 1) > -1, color='blue', alpha=.25)
plt.fill_between(X, -1, Y - 1, (Y - 1) < -1, color='red', alpha=.25)
plt.title('curve_chart2')
plt.show()
