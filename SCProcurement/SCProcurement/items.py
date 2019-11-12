# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScprocurementItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()
    linkhref = scrapy.Field()

class ULItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    linkhref = scrapy.Field()

class TableItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
