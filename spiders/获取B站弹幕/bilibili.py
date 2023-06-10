#!/usr/bin/env python
# encoding: utf-8
# 使用import导入requests模块
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 从pyecharts.charts中导入Line模块
from pyecharts.charts import Line

# 将https://comment.bilibili.com/218710655.xml赋值给变量url
url = "https://comment.bilibili.com/218710655.xml"

# 将变量url作为参数，添加进requests.get()中，给赋值给response
response = requests.get(url)

# 调用.encoding属性获取requests模块的编码方式
# 调用.apparent_encoding属性获取网页编码方式
# 将网页编码方式赋值给response.encoding
response.encoding = response.apparent_encoding

# 将服务器响应内容转换为字符串形式，赋值给xml
xml = response.text

# 使用BeautifulSoup()读取xml，添加lxml解析器，赋值给soup
soup = BeautifulSoup(xml, "lxml")

# 使用find_all()查询soup中d的节点，赋值给content_all
content_all = soup.find_all(name="d")

# 新建一个列表timeList
timeList = []

# for循环遍历content_all
for comment in content_all:
    # 使用.attrs获取p对应的属性值，并赋值给data
    data = comment.attrs["p"]

    # 使用split()函数分割data，获取时间并赋值给time
    time = data.split(",")[0]

    # 将time转换成浮点数，添加进列表timeList中
    timeList.append(float(time))

# 新建一个字典subtitlesDict
subtitlesDict = {}

# 使用for循环遍历range()函数生成的0-24的数字
for x in range(25):
    # 将30*x+1赋值给变量start
    start = 30 * x + 1

    # 将30*(x+1)赋值给变量end
    end = 30 * (x + 1)

    # 格式化start和end
    # 用短横线相连，赋值给segment_range
    segment_range = f"{start}-{end}"

    # 将segment_range作为字典subtitlesDict的键,添加进字典中
    # 将字典中键所对应的值设置为0
    subtitlesDict[segment_range] = 0

# for循环遍历字典subtitlesDict所有的键
for subtitle in subtitlesDict.keys():

    # 使用split()分隔字典的键获取第一项，赋值给变量start_key
    start_key = subtitle.split("-")[0]

    # 使用split()分隔字典的键获取第二项，赋值给变量end_key
    end_key = subtitle.split("-")[1]

    # for循环遍历列表timeList
    for item in timeList:

        # 如果弹幕分布时间在整型start_key和整型end_key之间
        if int(start_key) <= item <= int(end_key):
            # 将字典中键所对应的值累加
            subtitlesDict[subtitle] = subtitlesDict[subtitle] + 1

# 使用Line()创建Line对象，赋值给line
line = Line()

# 使用list()将字典subtitlesDict所有键转换成列表，传入add_xaxis()中
line.add_xaxis(list(subtitlesDict.keys()))

# 使用add_yaxis()函数，将数据统称设置为"弹幕数"
# 将字典subtitlesDict所有值转换成列表，作为参数添加进函数中
line.add_yaxis("弹幕数", list(subtitlesDict.values()))

# 使用render()函数存储文件，设置文件名为line.html
line.render("line.html")

# 使用print输出success
print("success")
