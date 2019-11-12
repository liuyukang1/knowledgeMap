from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TableItem
import json

class BaseSpider(CrawlSpider):
    name = 'BaseSpider'
    start_urls = ['http://www.ccgp-sichuan.gov.cn']

    # 首頁解析，獲取招標大類地址
    link = LinkExtractor(allow=r'channelCode=sjcg')

    # 獲得市級公告列表地址
    link_shiji = LinkExtractor(allow=r'shiji_')

    # 解析器
    rules = (
        Rule(link, callback='parse_item', follow=True, ),
        Rule(link_shiji, callback='parse_ul', follow=True, ),
    )

    def parse_item(self, response):
        pass

    def parse_ul(self, response):
        item = TableItem()
        title = response.xpath('//div/div/h1/text()').get()
        content = {}
        for each in response.xpath('//div/div/div/table/tbody/tr'):
            key = each.xpath('./td[1]/text()').get()
            value = each.xpath('./td[2]/text()').get()
            content[key] = value
        item['title'] = title
        item['content'] = content

        print(item)
        yield item


