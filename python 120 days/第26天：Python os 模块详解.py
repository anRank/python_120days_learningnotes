# 导入os模块时要注意，b不要j将os模块包导入，即不要使用from os import *导入os模块
# 否则os.open()j将会覆盖内置函数open()
# 读写文件：内置函数open()
# 路径相关操作：os的子模块os.path
# 逐行读取多个文件：fileinput模块
# 创建l临时文件或路径：tempfile模块
# 更高级的文件和路径操作：shutil模块

# os.name
import os

print(os.name)
# 有效名称：posix、nt、java
# posix是Portable Operating System Interface of UNIX（可移植操作系统接口）的缩写。Linux 和 Mac OS 均会返回该值；
# nt全称应为“Microsoft Windows NT”，大体可以等同于 Windows 操作系统，因此 Windows 环境下会返回该值；
# java则是 Java 虚拟机环境下的返回值。

# os.environ
# os.environ返回环境相关的信息，主要是各类环境变量。
# 返回值是一个映射（类似字典类型），具体的值为第一次导入os模块时的快照；其中的各个键值对，键是环境变量名，值则是环境变量对应的值。
print(os.environ['HOMEPATH'])

# os.walk()
# 这个函数需要传入一个路径作为top参数，函数的作用是在以top为根节点的目录树中游走，
# 对树中的每个目录生成一个由(dirpath, dirnames, filenames)三项组成的三元组。
# dirpath是一个指示这个目录路径的字符串，
# dirnames是一个dirpath下子目录名（除去“.”和“..”）组成的列表，
# filenames则是由dirpath下所有非目录的文件名组成的列表。
for item in os.walk("."):
    print(item)


# os.listdir()
# listdir即list directories：列出当前目录下的全部路径及文件。
# 该函数存在一个参数，用以指定要列出子目录的路径，默认为“.”，即“当前路径”。
# 函数返回值是一个列表，其中各元素均为字符串，分别是各路径名和文件名。
# 通常在需要遍历某个文件夹中文件的场景下极为实用。
def get_filelists(file_dir='.'):
    list_directory = os.listdir(file_dir)
    filelists = []
    for directory in list_directory:
        if os.path.isfile(directory):
            filelists.append(directory)
    return filelists


# os.mkdir()
# make directory，用处是“新建一个路径”。
# 需要传入一个类路径参数用以指定新建路径的位置和名称，如果指定路径已存在，则会抛出FileExistsError异常。
os.mkdir("test_os_mkdir")
# 在需要新建多级路径的场景下，可以使用os.makedirs()。
# 函数os.makedirs()执行的是递归创建，若有必要，会分别新建指定路径经过的中间路径，直到最后创建出末端的“叶子路径”。
os.makedirs("test_os_mkdir/test_os_makedirs/just/do/python/hello")

# os.remove()
# 用于删除文件，如果指定路径是目录而非文件的话，就会抛出IsADirectoryError异常。
# 删除目录应该使用os.rmdir()函数。
# 对应于os.makedirs()，删除路径操作os.rmdir()也有一个递归删除的函数os.removedirs()，
# 该函数会尝试从最下级目录开始，逐级删除指定的路径，几乎就是一个os.makedirs()的逆过程

# os.rename()
# 调用格式为os.rename(src, dst)
# src指向的文件或路径重命名为dst指定的名称。

# os.getcwd()
# get the current working directory 获取当前工作路径
print(os.getcwd())

# os.chdir()
# change the directory os.chdir()的用处实际上是切换当前工作路径为指定路径。


# os.path模块
# 这个模块是os模块根据系统类型从另一个模块导入的，并非直接由os模块实现，
# 比如os.name值为nt，则在os模块中执行import ntpath as path
import ntpath as path

# os.path.join()
# 将多个传入路径组合为一个路径。实际上是将传入的几个字符串用系统的分隔符连接起来，组合成一个新的字符串，
print(os.path.join("just", "do", "python", "dot", "com"))

# os.path.abspath()
# 将传入路径规范化，返回一个相应的绝对路径格式的字符串。
os.path.abspath("a:/just/do/python")

# os.path.basename()
# 该函数返回传入路径的“基名”，即传入路径的最下级目录。
os.path.basename("/ityouknow/justdopython/IAmBasename")
# 我的系统中同样没有这么一个路径。可见 os.path.basename() 页也是单纯进行字符串处理

# os.path.dirname()
os.path.dirname
os.path.dirname("/ityouknow/justdopython/IAmBasename")


# os.path.split()
# 将传入路径以最后一个分隔符为界，分成两个字符串，并打包成元组的形式返回。
# 前两个函数os.path.dirname()和os.path.basename()的返回值分别是函数os.path.split()返回值的第一个、第二个元素。
def basename(p):
    """Returns the final component of a pathname"""
    return os.path.split(p)[1]


def dirname(p):
    """Returns the directory component of a pathname"""
    return os.path.split(p)[0]


# os.path.exists()
# 用于判断路径所指向的位置是否存在。
print(os.path.exists("."))

# os.path.isabs()
# 判断是否是绝对路径
print(os.path.isabs("a:/justdopython"))

# os.path.isfile() os.path.isdir()
# 判断传入路径是否是文件或路径
os.path.isfile("a:/justdopython")
os.path.isdir("a:/justdopython/")