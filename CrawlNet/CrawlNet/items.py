# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# item定义存储字段:
import scrapy

class BossItem(scrapy.Item):
    title = scrapy.Field()
    downloadlink = scrapy.Field()

