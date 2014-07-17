# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JazzScraperItem(scrapy.Item):
    date = scrapy.Field()
    description = scrapy.Field()
    outdoor = scrapy.Field()
