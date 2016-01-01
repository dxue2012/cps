# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CpsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()  # name of the puzzle
    FEN = scrapy.Field()  # FEN representation of the puzzle
    # solution = scrapy.Field()  # solution of the puzzle
