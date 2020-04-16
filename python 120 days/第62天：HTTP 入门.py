# HTTP 超文本传输协议 HyperText Transfer Protocol
# 1.协议的必要性
# 机器完整、准确提取信息

# 2.URL
# Uniform Resource Locator 统一资源定位符
# URI：Uniform Resource Indentifier 统一资源定位符
# URL是URI的真子集，一个URL一定是URI，但URI不一定是URL
# 如果某个URL指定的文件就在与客户端直接通信的主机上，那么只需使用文件在该主机上的绝对路径即可区别这个文件；
# 此时的URI就可以是这个绝对路径，比对应的URL更加简短。
# 但如果与客户端直接通信的主机仅仅是y一个代理（中转），此时只使用绝对路径是不够的，还需指明是哪台主机。
# 这种情况下，URI和URL就相等了。
# 例：http://www.justdopython.com/2019/04/04/writing-specifications/
# 分解如下：
# http:
# //
# www.justdopython.com
# /2019/04/04/writing-specifications/
# http：表明使用的是HTTP协议进行通信
# www.justdopython.com：称为"域名"，可以简单理解为互联网上的某一台主机。
# /2019/04/04/writing-specifications/：请求资源在这台主机上的路径

# HTTP协议的格式
# 整体划分为两大类：请求、响应
# HTTP协议格式主要分成四个部分：起始行、消息头、空行、消息体
# 起始行　包含３个信息：方法、URI、HTTP协议版本
# 方法：本次请求要执行的操作。常见的方法是：GET、POST
# GET：表示客户端要从服务器获取资源
# POST：b表示客户端要想服务器传输一些表单数据
