#!/usr/bin/env python
# encoding: utf-8
# 使用import导入requests模块
import requests
# 使用from...import从bs4模块中导入BeautifulSoup
from bs4 import BeautifulSoup
# 使用import导入json模块
import json

# 复制网页链接赋值给变量url
url = "https://search.jd.com/Search?keyword=%E5%B7%A7%E5%85%8B%E5%8A%9B&enc=utf-8&wq=%E5%B7%A7%E5%85%8B%E5%8A%9B&pvid=dd65926ff30441409a11eceb998167db"

# 将User-Agent以字典键值对形式赋值给headers
# 将cookie以字典键值对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    "cookie":"shshshfpa=59756f24-6de8-90a9-92f3-022a321cbcaa-1589969605; __jdu=1589969605288365795565; shshshfpb=fZNp5OzH0j2T%20X%20WnJhzrBg%3D%3D; qrsc=3; user-key=b05356ef-c40b-44d2-a837-60df17e9b74e; cn=0; _pst=jd_51aaae03cedfa; unick=jd_51aaae03cedfa; pin=jd_51aaae03cedfa; _tp=FNP1fTo2ON7jgdbikn0lWAbSqMI20pF0xO0Iq%2FccQVc%3D; pinId=qN40m03yULDpSLzjaHwm07V9-x-f3wj7; __jdc=122270672; rkv=1.0; 3AB9D23F7A4B3C9B=DVCEDHG6BLYWMZMJIWNBOSTWP7GOWK77C5VJKGVQO7F3JHUFZVL5V5B5UKDYLF2LK5VAEIOSN2YRG33EJLXR6ZJ2TU; __jdv=122270672|direct|-|none|-|1602475191357; areaId=22; ipLoc-djd=22-1930-50947-0; __jda=122270672.1589969605288365795565.1589969605.1602487075.1602569356.29; shshshfp=b393a5ab6c1163583435b3a90574cb22; shshshsID=ef428a912dae95ba61fd7ac2ee0af172_9_1602570753319; __jdb=122270672.9.1589969605288365795565|29.1602569356"
    }

# 使用get()函数请求链接，并且带上headers
response = requests.get(url, headers=headers)
# 使用.text属性将服务器相应内容转换为字符串形式，赋值给html
html = response.text
# 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html, "lxml")
# 使用find_all()查询soup中class="gl-item"的节点，赋值给content_all
content_all = soup.find_all(class_="gl-item")
# 使用for循环遍历content_all
for content in content_all:

    # 使用.attrs属性获取data-sku对应的属性值，并赋值给p_id
    p_id = content.attrs["data-sku"]
    # 取出每个商品编号，用格式化字符串的方式，拼接出新的链接，赋值给url
    url = f"https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={p_id}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=9d8a323c646add49&fold=1"
    # 使用get()函数请求链接，并且带上headers，赋值给res
    res = requests.get(url, headers=headers)
    # 使用.text属性将响应消息转换成字符串，赋值给html
    html = res.text
    # 使用lstrip()移除左侧的"fetchJSON_comment98("，赋值给html
    html = html.lstrip("fetchJSON_comment98(")
    # 使用rstrip()移除右侧的);，赋值给html
    html = html.rstrip(");")
    # 使用json.loads()将str转换成dict型，赋值给json_data
    json_data = json.loads(html)
    # 使用"hotCommentTagStatistics"键获取对应的值，赋值给data
    data = json_data["hotCommentTagStatistics"]

    # 定义一个字典p_dict用于存放每个商品的标签信息
    p_dict = {}

    # 使用for循环遍历列表data中的每一项
    for item in data:
        # 提取键name对应的值，赋值给name
        name = item["name"]
        # 提取count对应的值，赋值给count
        count = item["count"]
        # 按 评价:数量 的方式写入到字典中
        p_dict[name] = count

    # 使用with...as语句配合open()函数打开文件商品信息.txt
    # 将打开的文件设置为f
    with open("商品信息.txt", "a") as f:
        # 使用write()函数写入商品信息
        # 使用str()将字典转为字符串格式
        # 每写完一个换行"\n"
        f.write(str(p_dict)+"\n")