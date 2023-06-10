#!/usr/bin/env python
# encoding: utf-8
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


def get_list_data(offset):
    """
    获取房源列表数据
    :param offset: 页数
    :return:
    """
    links = []  # 超链接
    URL = 'https://sh.ke.com/ershoufang/su1y1f2a3a4/pg{}/#contentList'.format(offset)

    User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'
    header = {
        "User-Agent": User_Agent
    }
    html = requests.get(URL, headers=header).text  # 网络请求
    soup = BeautifulSoup(html, "html.parser")
    content_len = len(soup.find_all('div', class_='info clear'))
    # 保存所有超链接
    f = open('links.txt', 'a')
    for i in range(content_len):
        link = soup.find_all('div', class_='info clear')[i].find_all('a', class_="VIEWDATA CLICKDATA maidian-detail")[
            0].get('href')
        links.append(link)
        f.write(json.dumps(link, ensure_ascii=False) + '\n')
    f.close()
    return links


def get_detail_data(links, data):
    """
    获取房源详细数据
    :param link: 超链接
    :return:
    """
    for link in links:
        print(link)
        User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'
        header = {
            "User-Agent": User_Agent
        }
        html = requests.get(link, headers=header).text
        parse_html(html, data)


def parse_html(html, data):
    """
    解析房源的html数据为具体数据
    :param html: html数据
    :param data: 需要保存的列表数据
    :return:
    """
    soup = BeautifulSoup(html, "html.parser")
    try:
        title = soup.find_all('h1', class_="main")[0].get('title')
    except:
        title = ''
    community_name = remove_stop_word(soup.find_all('div', class_="communityName")[0].text)
    unit_price = soup.find_all('span', class_="unitPriceValue")[0].text
    total_price = soup.find_all('span', class_="total")[0].text
    floor_info = soup.find_all('div', class_="subInfo")[0].text
    room_info = soup.find_all('div', class_="room")[0].find_all('div', class_="mainInfo")[0].text
    type_info = soup.find_all('div', class_="type")[0].find_all('div', class_="mainInfo")[0].text
    area = soup.find_all('div', class_="area")[0].find_all('div', class_="mainInfo")[0].text
    address_name = soup.find_all('div', class_="areaName")[0].find_all('a')[0].text
    try:
        address_sub_name = soup.find_all('div', class_="areaName")[0].find_all('a')[1].text
    except:
        address_sub_name = ''
    try:
        introContent_name = remove_stop_word(
            soup.find_all('div', class_="baseattribute clear")[0].find_all('div', class_="content")[
                0].text)
    except:
        introContent_name = ''

    try:
        surrounding_supporting = \
            remove_stop_word(soup.find_all('div', class_="baseattribute clear")[2].find_all('div', class_="content")[
                                 0].text)
    except:
        surrounding_supporting = ''
    try:
        transportation = remove_stop_word(
            soup.find_all('div', class_="baseattribute clear")[3].find_all('div', class_="content")[0].text)
    except:
        transportation = ''
    data_dict = {
        "title": title,
        "community_name": community_name,
        "unit_price": unit_price,
        "total_price": total_price,
        "floor_info": floor_info,
        "room_info": room_info,
        "type_info": type_info,
        "area": area,
        "address_name": address_name,
        "address_sub_name": address_sub_name,
        "introContent_name": introContent_name,
        "surrounding_supporting": surrounding_supporting,
        "transportation": transportation
    }
    f = open('data.txt', 'a')

    f.write(json.dumps(data_dict, ensure_ascii=False) + '\n')
    f.close()
    data.append(data_dict)


def save_data(data):
    """
    保存数据到excel
    :param data: 保存数据集
    :return:
    """
    pf = pd.DataFrame(data)
    columns_map = {
        "title": '标题',
        "community_name": '小区名称',
        "unit_price": '单价',
        "total_price": '总价',
        "floor_info": '楼层信息',
        "room_info": '房间信息',
        "type_info": '朝向',
        "area": '面积',
        "address_name": '区域',
        "address_sub_name": '地址',
        "introContent_name": '核心卖点',
        "surrounding_supporting": '周边配置',
        "transportation": '交通出行'
    }
    pf.rename(columns=columns_map, inplace=True)
    # 将空的单元格替换为空字符
    pf.fillna('', inplace=True)
    pf.to_excel('上海二手房数据.xlsx', encoding='utf-8', index=False)


def remove_stop_word(data):
    """
    删除停用词
    :param data: 源数据
    :return:
    """
    data = data.replace('\n', '')
    data = data.replace('小区名称', '')
    data = data.replace('地图', '')
    data = data.replace(' ', '')
    data = data.replace('   ', '')
    return data


if __name__ == '__main__':
    data = []
    for i in range(1, 5):
        print("爬虫第{}页数据...".format(str(i)))
        # 获取房源列表数据
        links = get_list_data(i)
        # 获取房源详细数据
        get_detail_data(links, data)
    # 导出数据集
    save_data(data)
    print('爬虫结束')
