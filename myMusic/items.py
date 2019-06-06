# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MymusicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 图片地址
    imgSrc = scrapy.Field()
    # 标题中文
    titleCn = scrapy.Field()
    # 标题英文
    titleEn = scrapy.Field()
    # 详情页url
    url = scrapy.Field()
