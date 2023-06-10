#!/usr/bin/env python
# encoding: utf-8

# 从pyecharts.charts中导入Bar模块
from pyecharts.charts import Bar

# 使用with...as语句配合open()函数以r方式，打开路径为“/Users/tongtong/职位数据.txt”的文件，赋值给f
with open("职位数据.txt", "r") as f:

    # 使用readlines()读取f中的所有行，赋值给dataList
    dataList = f.readlines()

# 新建一个字典cityDict
cityDict = {}

# for循环遍历列表dataList中的每个元素data
for data in dataList:

    # 如果"薪资面议"在元素中
    if "薪资面议" in data:
        # 就跳过
        continue

    # 使用split()以逗号分隔data，索引第3项元素，赋值给city
    city = data.split(",")[2]

    # 使用split()以逗号分隔data，索引第4项元素，赋值给salary
    salary = data.split(",")[3]

    # 使用split()以斜杠分隔salary，索引第1项元素，赋值给daily
    daily = salary.split("/")[0]

    # 使用split()以短横线分隔daily索引第1项，赋值给start
    start = daily.split("-")[0]
    # 使用split()以短横线分隔daily索引第2项，赋值给end
    end = daily.split("-")[1]

    # 将start和end转换成整型相加后除以2，并赋值给average
    average = (int(start)+int(end))/2

    # 如果city不在字典cityDict的键中
    if city not in cityDict.keys():

        # 将字典中键所对应的值设置为空列表
        cityDict[city] = []

    # 使用append()函数往字典键所对应的值中添加average
    cityDict[city].append(average)

# 新建一个字典city_num_dict
city_num_dict = {}

# for循环遍历cityDict.items()中的key,value
for key,value in cityDict.items():

    # 使用sum()函数将列表value求和
    # 使用len()函数计算列表value长度
    # 使用//运算符计算列表value的平均值，赋值给average_value
    average_value = sum(value)//len(value)

    # 将字典cityDict的键对应的值设置为average_value
    cityDict[key] = average_value

    # 将字典city_num_dict的键设置为不同城市
    # 将对应的值设置为len(value)
    city_num_dict[key] = len(value)

# 创建Bar对象，赋值给bar
bar = Bar()

# 使用list()将字典cityDict所有键转换成列表，传入add_xaxis()中
bar.add_xaxis(list(cityDict.keys()))

# 使用add_yaxis()函数，将数据统称设置为"城市"
# 将字典cityDict所有值转换成列表，作为参数添加进函数中
bar.add_yaxis("城市",list(cityDict.values()))

# 使用render()函数存储文件，设置文件名为salary.html
bar.render("salary.html")

# 创建Bar对象，赋值给bar_city
bar_city = Bar()

# 使用list()将字典city_num_dict所有键转换成列表，传入add_xaxis()中
bar_city.add_xaxis(list(city_num_dict.keys()))

# 使用add_yaxis()函数，将数据统称设置为"城市"
# 将字典city_num_dict所有值转换成列表，作为参数添加进函数中
bar_city.add_yaxis("城市",list(city_num_dict.values()))

# 使用render()函数存储文件，设置文件名为positions.html
bar_city.render("positions.html")