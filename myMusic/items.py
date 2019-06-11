# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AlbumItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 图片地址
    imgSrc = scrapy.Field()
    # 标题中文
    titleCn = scrapy.Field()
    # 标题英文
    titleEn = scrapy.Field()
    # 是否是album
    isAlbum = scrapy.Field()


class SongItem(scrapy.Item):
    # 低质量地址
    lowUrl = scrapy.Field()
    # 高质量地址
    highUrl = scrapy.Field()
    # 曲子的标题
    subTitle = scrapy.Field()
    # 图片地址
    imgSrc = scrapy.Field()
    # 序号
    serial = scrapy.Field()