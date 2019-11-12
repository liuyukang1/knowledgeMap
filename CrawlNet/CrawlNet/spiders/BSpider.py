# spider编码:
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BossItem

class BSpider(CrawlSpider):
    name = 'CrawlNet'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.ygdy8.net/html/gndy/oumei/index.html']
    # 定义两个链接提取器，分别为首页和详情页的
    # 由于我们不需要首页的内容，所以首页的链接提取器pass
    link = LinkExtractor(allow=r'list.*?html')
    link_detail = LinkExtractor(allow=r'.*?/\d+\.html')
    # 两个函数为解析器
    rules = (
        Rule(link, callback='parse_item', follow=True,),
        Rule(link_detail, callback='parse_detail', follow=True,),
    )

    def parse_item(self, response):
        pass

    def parse_detail(self, response):
        title = response.xpath('//h1//text()').extract_first()
        downloadlink = response.xpath('//tbody/tr/td/a/text()').extract_first()
        if title and downloadlink and 'ftp' in downloadlink:
            item = BossItem()
            item['title'] = title
            item['downloadlink'] = downloadlink
            yield item
