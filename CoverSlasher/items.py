# -*- coding: utf-8 -*-


import scrapy


class CoverslasherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_urls = scrapy.Field()  #保存图片地址
    images = scrapy.Field()      #保存图片的信息
    image_names = scrapy.Field()      #保存图片的信息
