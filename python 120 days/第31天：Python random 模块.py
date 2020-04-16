import random

# random()函数
# random()函数可以随机生成y一个[0, 1)的浮点数：
print(random.random())

# random(a,b)函数
print(random.uniform(2, 5))
print(random.uniform(5, 2))

# sample(sequence, k)函数
# 获取从总体序列或集合中选择的唯一元素的k长度列表。
# sample()函数不会修改原有序列, 它主要用在无重复的随机抽样场景, 实现从大量样本中快速进行抽样：
lst = [1, 2, 3, 4, 5]
print(random.sample(lst, 4))
print(lst)

# randrange([start],stop[,step])函数
# 返回一个随机数
# randrange([start], stop) 指定范围生成随机数
print(random.randrange(2, 5))

# randrange([start], stop[, step])
# 函数可以先从1到10中产生一个间隔是2的等差数列[1,3,5,7,9]，再从中随机获取一个随机数。
print(random.randrange(1, 10, 2))

# choice(sequence)函数
# 从非空序列 sequence 中随机返回一个数，参数 sequence 表示一个有序类型，可以包含 list、tuple 等。
strlist = ['C++', 'C#', 'Java', 'Python']
strtemp = 'Do you love python'
print(random.choice(strlist))
print(random.choice(strtemp))

# shuffle(x[, random])函数
# 将一个有序l列表中的元素打乱，再重新排序
lst = ['A', 'B', 'C', 'D', 'E']
random.shuffle(lst)
print(lst)