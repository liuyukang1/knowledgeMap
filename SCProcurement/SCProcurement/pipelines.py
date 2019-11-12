# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class ScprocurementPipeline(object):
    def __init__(self):
        self.file = codecs.open('data.json', mode='wb', encoding='utf-8')

    def process_item(self, item, spider):
        t = dict(item)
        if (t.get('title') != None and t.get('content') != {}):
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.file.write(line)
        return item
