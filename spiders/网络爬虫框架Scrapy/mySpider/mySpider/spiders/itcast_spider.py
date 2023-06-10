#!/usr/bin/env python
# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import scrapy
from mySpider.items import itcastItem


class ItcastSpider(scrapy.spiders.Spider):
    name = "itcast"
    allowed_domains = ["http://www.itcast.cn"]
    start_urls = [
        "http://www.itcast.cn/channel/teacher.shtml#ac"
    ]

    def parse(self, response):
        items = []
        for site in response.xpath('//div[@class="li_txt"]'):
            item = itcastItem()
            print "--------------"
            teacher_name = site.xpath('h3/text()').extract()
            teacher_level = site.xpath('h4/text()').extract()
            teacher_info = site.xpath('p/text()').extract()
            unicode_teacher_name = teacher_name[0].decode('utf-8')
            unicode_teacher_level = teacher_level[0].decode('utf-8')
            unicode_teacher_info = teacher_info[0].decode('utf-8')
            print unicode_teacher_name
            print unicode_teacher_level
            print unicode_teacher_info
            item['name'] = unicode_teacher_name
            item['level'] = unicode_teacher_level
            item['info'] = unicode_teacher_info
            items.append(item)
            print "--------------"