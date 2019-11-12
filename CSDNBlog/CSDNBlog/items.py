# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field


class CsdnblogItem(Item):
    """存储提取信息数据结构"""
    article_url = Field()
    article_name = Field()
