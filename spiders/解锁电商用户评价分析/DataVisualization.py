#!/usr/bin/env python
# encoding: utf-8
# 使用from...import从pyecharts.charts模块中导入Bar模块
from pyecharts.charts import Bar

# 将路径"/Users/jd/商品信息.txt"赋值给path
path = "/Users/jd/商品信息.txt"

# 使用with...as语句配合open()函数打开文件
# 打开方式设为只读
# 将打开的文件设为f
with open(path, "r") as f:
    # 使用readlines()函数读出商品信息文档中的内容，赋值给read_content
    read_content = f.readlines()

# 定义用于存储评价频次的字典comment_dict
comment_dict = {}

# 定义一个存储评价标签和被评价次数的字典comment_count
comment_count = {}

# 使用for循环遍历read_content
for content in read_content:
    # 使用strip()将\n移除，并赋值给content
    content = content.strip("\n")
    # 使用eval()函数将字符串转为字典类型，并赋值给content
    content = eval(content)
    # 使用items()将字典转成列表形式，并赋值给content_list
    content_list = content.items()

    # 使用for循环遍历content_list
    for key, value in content_list:

        # 判断键不在字典comment_dict中时
        if key not in comment_dict:
            # 将键写入字典，并设置值为1
            comment_dict[key] = 1
        else:
            # 将键对应的值加1
            comment_dict[key] += 1

        # 判断键不在字典comment_count中时
        if key not in comment_count:
            # 将值value写入字典
            comment_count[key] = value
        else:
            # 将值value加到comment_count[key]键对应的值中
            comment_count[key] = comment_count[key] + value

# 定义一个字典comment_count_new
comment_count_new = {}
# 使用items()将字典转成列表形式，并赋值给comment_count_list
comment_count_list = comment_count.items()

# 使用for循环变量列表
for key, value in comment_count_list:
    # 判断comment_count中键的值小于100时
    if comment_count[key] < 100:
        # 继续下次循环
        continue
    else:
        # 将键和值添加到comment_count_new字典中
        comment_count_new[key] = value

# 使用Bar()创建Bar对象，赋值给bar
bar= Bar()
# 使用list()将字典comment_dict所有键转换成列表，传入add_xaxis()中
bar.add_xaxis(list(comment_dict.keys()))
# 使用add_yaxis()函数，将数据统称设置为"评价频次"
# 将字典comment_dict所有值，作为参数添加进函数中
bar.add_yaxis("评价频次", list(comment_dict.values()))
# 使用render()函数存储文件，设置文件名为"comments.html"
bar.render("comments.html")


# 使用Bar()创建Bar对象，赋值给bar_total
bar_total = Bar()
# 使用list()将字典comment_count_new所有键转换成列表，传入add_xaxis()中
bar_total.add_xaxis(list(comment_count_new.keys()))
# 使用add_yaxis()函数，将数据统称设置为"总评价数"
# 将字典comment_count_new所有值，作为参数添加进函数中
bar_total.add_yaxis("总评价数", list(comment_count_new.values()))
# 使用render()函数存储文件，设置文件名为"count.html"
bar_total.render("count.html")