# namedtuple功能详解
from collections import namedtuple

# namedtuple()返回一个新的元组子类，规定元组的个数，同时除了下标获取元素外，还可以通过属性直接获取
User = namedtuple("User", ["name", "age", "weight"])
user = User("admin", "20", "60")
name, age, weight = user
print(user[0])
print(name, age, weight)
print(user.name, user.age, user.weight)
# namedyuple()相当于直接定义了一个新的类。返回值是一个tuple。

# 将序列转换为新的tuple对象
user = ["root", 32, 65]
user = User._make(user)
print(user)

# 返回一个dict
user = User("admin", 20, 60)
print(user._asdict())

# ChainMap功能详解
# ChainMap()可以将多个字典集合到一个字典中去，对外提供一个统一的视图。实际上是在多个字典的上层又进行了一次封装。
from collections import ChainMap

user1 = {"name": "admin", "age": 20}
user2 = {"name": "root", "weight": 65}
users = ChainMap(user1, user2)
print(users.maps)

users.maps[0]["name"] = "tiger"
print(users.maps)

for key, value in users.items():
    print(key, value)

# 如果ChainMap()中的多个字典有重复key，查看的时候可以看到所有的key，
# 但遍历的时候只会遍历key第一次出现的位置，其余的忽略。

# deque功能详解
# deque是类似list的容器，在两端k快速添加append和pop
from collections import deque

q = deque([1, 2, 3])
q.append(4)
q.appendleft(0)
print(q)
print(q.popleft())

# Counter功能详解
# Counter可以简单理解为计数器，可以统计每个元素出现的次数，同样Counter()需要接受一个可迭代的对象。
from collections import Counter

animals = ["cat", "dog", "cat", "bird", "horse", "tiger", "horse", "cat"]
animals_counter = Counter(animals)
print(animals_counter)
print(animals_counter.most_common(2))
# 其实Counter是一个字典，其额外提供的most_common()函数通常用于求Top k问题。

# OrderedDict功能详解
# OrderDict是字典的子类，保证了元素的插入顺序。
# 算法上，OrderedDict可以比dict更好地处理频繁的重新排序操作。在跟踪最近的访问这种场景下非常适用。
# OrderedDict类有一个move_to_end()方法，可以有效地将元素移动到任一端。
from collections import OrderedDict

user = OrderedDict()
user["name"] = "admin"
user["age"] = 23
user["weight"] = 65
print(user)
user.move_to_end("name")
print(user)
user.move_to_end("name", last=False)
print(user)

# defaultdict功能详解
# defaultdict是内置dict类的子类。它实现了当key不存在是返回默认值的功能，除此之外，与内置dict功能完全一样。
from collections import defaultdict

default_dict = defaultdict(int)
default_dict["x"] = 10
print(default_dict["x"])
print(default_dict["y"])


# defaultdictd的参数必须是可操作的。比如python内置类型，或者无参的可调用的函数。
def getUserInfo():
    return {
        "name": "",
        "age": 0
    }


default_dict = defaultdict(getUserInfo)
admin = default_dict["admin"]
print(admin)

admin["age"] = 34
print(admin)
