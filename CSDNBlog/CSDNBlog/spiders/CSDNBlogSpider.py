#!/usr/bin/python
# -*- coding:utf-8 -*-

# from scrapy.contrib.spiders import  CrawlSpider,Rule
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from ..items import CsdnblogItem


class CSDNBlogSpider(Spider):

    """爬虫CSDNBlogSpider"""
    name = "CSDNBlog"

    # 减慢爬取速度 为1s
    download_delay = 1
    allowed_domains = ["blog.csdn.net"]
    start_urls = [
        # 第一篇文章地址
        "https://www.csdn.net/nav/python"
    ]

    def parse(self, response):
        sel = Selector(response)

        for each in sel.xpath('//ul[@id="feedlist_id"]/li/div/div/h2/a'):
            # 获得文章url和标题
            item = CsdnblogItem()

            article_url = each.xpath('./@href').extract()[0]
            article_name = each.xpath('./text()').extract()[0]

            item['article_url'] = article_url.replace(' ', '')
            item['article_name'] = article_name.replace(' ', '')

            yield item
