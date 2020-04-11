# datetime()构造函数
from datetime import datetime
import time

# 当前日期和时间
print(datetime.now())

# 获取指定时间
datetest = datetime(2019, 9, 30, 22, 22, 0)
print(datetest)

# 获取日期的年月日时分秒
print(str(datetest.year) + "-" + str(datetest.month) + "-" + str(datetest.day) + " " + str(datetest.hour) + ":" + str(
    datetest.minute) + ":" + str(datetest.second))

# fromtimestamp()函数
# fromtimestamp()函数可以将时间戳转换成 datetime 对象。
dt1 = datetime.fromtimestamp(10000)
dt2 = datetime.fromtimestamp(time.time())
print(dt1)
print(dt2)

# strptime()和strftime()函数
# 使用strptime()函数可以将日期字符串转换成datetime类型，strftime()函数可以将datetime类型转换成字符串
# 日期转换
datestr = datetime.strptime('2019-9-30 22:10:00', '%Y-%m-%d %H:%M:%S')
now = datetime.now()
print(datestr)
print(now.strftime('%a, %b %d %H:%M'))

# timedata()函数
# timedata()函数返回一个timedata类型的数据，它表示y一段时间而不是一个时刻，多用于日期的增加和减少场景。
# 日期增加和减少
now = datetime.now()
print(now)
import datetime

newdate = now + datetime.timedelta(hours=10)
print(newdate)
newdate = now - datetime.timedelta(days=1)
print(newdate)

# time模块
# time模块的主要功能是读取系统时钟的当前时间。其中，time.time()和time.sleep是两个最常用的模块。
# time()函数
# time.time()函数返回的值是带小数点的，它表示从Unix纪元（1970年1月1日0点）到执行代码那一刻所经历的时间的秒数，这个数字称为UNIX纪元时间戳。
import time

print("当前时间戳为：", time.time())


# 在项目开发中，我们经常需要计算一段代码的执行时间，就可以用纪元时间戳来实现。
def calculateTime():
    item = 1
    for i in range(1, 100000):
        item = item + i
    return item


startTime = time.time()
result = calculateTime()
endTime = time.time()
print('计算结果：' + str(result))
print('执行时间：' + str(endTime - startTime))
# 在代码中，函数calculateTime()是需要执行的代码块，变量startTime表示开始时间，变量endTime表示结束时间，endTime-startTime表示代码块运行的时间间隔

# sleep()函数
# 如果需要让程序暂停一下，可以使用time.sleep()函数。sleep()函数有个参数，表示需要暂停的秒数。
for i in range(2):
    print('one')
    print(time.time())
    time.sleep(1)
    print('two')
    print(time.time())
    time.sleep(1)
print("运行完成")
