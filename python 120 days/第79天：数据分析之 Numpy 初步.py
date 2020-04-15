import numpy as np
import matplotlib.pyplot as plt

# 通过列表创建数组
first_array = np.array([2, 3, 4])
print(first_array)
# dtype属性指明多维数组中y元素的类型
print(first_array.dtype)

example_list = [2.0, 3.0, 4.0]
second_array = np.array(example_list)
print(second_array)
print(second_array.dtype)

# a = np.array(1,2,3,4)
# a = np.array([1,2,3,4])

# 同为序列类型，元组也可以起到相同的作用：
a = np.array((2, 3, 4))
print(a)

# 如果提供的序列对象是嵌套的，numpy还可以直接生成更高伟的多维数组：
a = np.array(((2, 3, 4, 5,), (4, 5, 6, 7)))
print(a)
a = np.array([(2, 3, 4, 5), (4, 5, 6, 7)])
print(a)

# 在创建数组的同时显式指定数据类型：
complex_array = np.array([[1, 2], [3, 4]], dtype='complex')
print(complex_array)

# 元素未知的创建方式
# 知道多维数组的大小，不知道元素具体的值
# zeros创建的是全为0的多维数组，ones创建的是全为1的多维数组，empty创建随机初始值的多维数组
print(np.zeros((3, 4)))
print(np.ones((3, 4)))
print(np.empty((3, 4)))
print(np.empty((3, 5)))

# 等差序列的数组
# numpy提供arange函数，用以创建由等差序列组成的数组：
print(np.arange(10, 30, 5))
print(np.arange(0, 2, 0.3))
print(np.arange(0.2, 0.3, 0.01))

# 元素数量固定的浮点数组
# linspace与arange的区别在于第3个参数
# linspace为最终得到的元素个数
# arange为元素间的步长
print(np.linspace(0.2, 0.3, 9))

# 多维数组的基本属性
# 在numpy中，维度又被称为轴（axe）
# 基本属性：
# ndim：dn dimension 指示多维数组的维度，轴数
# shape：指示多维数组整体的维度，整体的形状。如n行m列，shape为(n, m)
# size：多维数组中y元素的总个数
# dtype：data type 多维数组中元素的数据类型
# itemsize：每个元素的字节大小。等效于dtype.itemsize
# data：包含多维数组中元素实际内存的缓冲区。

# 数组的打印形式
# 最后一个轴从左往右打印
# 次后轴从上往下打印
# 剩下的轴从上往下打印，每部分由一个空行隔开
print(np.zeros((2,)))
print(np.zeros((2, 3)))
print(np.zeros((2, 3, 4)))
print(np.zeros((2, 3, 4, 5)))

# 重整多维数组的大小
# reshape将多维数组重整为某个大小
print(np.arange(12))
print(np.arange(12).reshape(2, 6))
print(np.arange(12).reshape(6, 2))
# reshape允许缺省1个参数（用-1占位），根据数组元素的总数和提供的其他自动求出一个合适的值
print(np.arange(12).reshape(2, -1, 2))

# 多维数组的索引
# 一维数组索引
x = np.arange(10)
print(x[2])
print(x[-2])
# 对于二维和更高维的数组，可以在同一个括号内直接索引
x.shape = (2, 5)  # 等同于x = x.reshape(2, 5)
print(x[1, 3])
print(x[1, -1])
# 当给出的索引少于数组维数（轴数）时，得到一个数组对象：
print(x[0])

# 数组可以像列表一样，进行切片：
x = np.arange(10)
print(x[2:5])
print(x[1:7:2])

# numpy中的广播
# numpy中，各种运算默认都是逐元素的，如两个大小相同的数组运算:
a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0])
print(a * b)

# 广播的前提：相容的形状
# 1.两个数组各个维度相等 or 2.其中一个数组的对于维度为1（不存在的维度也为1）
# 例：一个多维数组和一个y一维数组的运算：
a = np.array([[0.0, 0.0, 0.0],
              [10.0, 10.0, 10.0],
              [20.0, 20.0, 20.0],
              [30.0, 30.0, 30.0]])
b = np.array([1.0, 2.0, 3.0])
print(a.shape)
print(b.shape)
print(a + b)

# 多维数组切片之图像裁剪
image = plt.imread("./img/python-logo.png")
print(image.shape)
image_crop = image[300:, ::, ::]
plt.imshow(image_crop)
plt.show()