# -*- coding: utf-8 -*-
import scrapy
import re

class MydouyinSpider(scrapy.Spider):
    name = 'mydouyin'
    allowed_domains = ['iesdouyin.com']
    start_urls = ['https://www.iesdouyin.com/share/user/88445518961?timestamp=1548046967']

    # v.douyin.com / NT5Nck /

    def parse(self, response):
        print("*"*30)
        text=response.xpath("//*[@id='pagelet-user-info']/div[2]/div[1]/p[2]/i[*]")

        # print(text)
        # print("*" * 30)
        # http://fontstore.baidu.com/static/editor/index.html
        dict1={'602':'1','60e':'1','618':'1',
               '603':'0','60d':'0','616':'0',
               '604':'3', '611':'3', '61a': '3',
               '605': '2', '610': '2', '617': '2',
               '606': '4', '60c': '4', '619': '4',
               '607': '5','60f': '5', '61b': '5',
               '608': '6', '612': '6', '61f': '6',
               '609': '9', '615': '9', '61e': '9',
               '60a': '7', '613': '7', '61c': '7',
               '60b': '8', '614': '8', '61d': '8',
               '78': 'x'}
        for key,values in dict1.items():
            print('key:',key)
            print('valus:',values)
            # text=re.sub(key,values,text)
            print(text)
            print(type(text))


# redis-server redis.conf