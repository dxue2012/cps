# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem


class DedupPipeline(object):
    def __init__(self):
        self.items_seen = set()

    def process_item(self, item, spider):
        if item['FEN'] in self.items_seen:
            raise DropItem("Duplicate puzzle found: %s" % item)
        else:
            self.items_seen.add(item['FEN'])
            return item
