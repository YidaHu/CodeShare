#!/usr/bin/env python
# encoding: utf-8
# 使用import导入requests模块
import requests
# 使用from...import从bs4模块中导入BeautifulSoup模块
from bs4 import BeautifulSoup
# 使用import导入time模块
import time
# 使用import导入pandas模块，并使用as简写为pd
import pandas as pd

# 将User-Agent以字典键对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}
# 使用EXcelWriter()函数打开 /Users/美食排行.xlsx 文档，赋值给writer
writer = pd.ExcelWriter("/Users/美食排行.xlsx")

# 使用for循环遍历10065和10099两个城市的代码
for city in ["10065", "10099"]:

    # 定义列表title_list用于存储店铺名称
    title_list = []
    # 定义列表score_list用于存储评分
    score_list = []
    # 定义列表review_list用于存储点评数据
    review_list = []

    # 使用for循环和range()函数，遍历1-10
    for page in range(1, 11):
        # 使用time.sleep()控制，每次循环停顿1秒
        time.sleep(1)

        # 使用格式化拼接城市编号和页数编号，赋值给url
        url = f"http://www.mafengwo.cn/cy/{city}/0-0-0-0-0-{page}.html"
        # 使用requests.get()请求内容，获取响应消息，赋值给response
        response = requests.get(url, headers=headers)
        # 使用.text属性将服务器相应内容转换为字符串形式，赋值给html
        html = response.text
        # 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
        soup = BeautifulSoup(html, "lxml")
        # 使用find_all()查询soup中class="item clearfix"的节点，赋值给content_all
        content_all = soup.find_all(class_="item clearfix")

        # for循环遍历content_all
        for content in content_all:
            # 使用find()查询content中的class="grade"的节点
            # 获取em节点的.string属性，赋值给score
            score = content.find(class_="grade").em.string
            # 使用append()函数将分数追加到score_list中
            score_list.append(score)

            # 使用find()查询content中的class="rev-num"的节点
            # 获取em节点的.string属性，赋值给review
            review = content.find(class_="rev-num").em.string
            # 使用append()函数将点评数追加到review_list中
            review_list.append(review)

            # 使用find()查询content中的class="title"的节点
            # 获取h3节点下的a节点的.string属性，赋值给title
            title = content.find(class_="title").h3.a.string
            # 使用append()函数将店铺名称追加到title_list中
            title_list.append(title)

    # 先将获取的列表信息转换成字典类型，赋值给total
    # "名称":title_list, "评分":score_list, "点评数量":review_list
    total = {"名称": title_list, "评分": score_list, "点评数量": review_list}
    # 将total传入DataFrame()函数，赋值给info
    info = pd.DataFrame(total)

    # 使用if判断，遍历10065北京的编号时
    if city == "10065":
        # 使用to_excel将信息写入writer文档中，并设置工作表名称为sheet_name="北京美食"
        info.to_excel(writer, sheet_name="北京美食")
    else:
        # 使用to_excel将信息写入writer文档中，并设置工作表名称为sheet_name="上海美食"
        info.to_excel(writer, sheet_name="上海美食")

# 使用save()函数保存文档
writer.save()
# 使用close()函数关闭文档
writer.close()
