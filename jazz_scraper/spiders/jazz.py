# -*- coding: utf-8 -*-
import scrapy

from ..items import JazzScraperItem


class JazzSpider(scrapy.Spider):
    name = "jazz"
    allowed_domains = ["umbriajazz.com"]
    start_urls = (
        'http://www.umbriajazz.com/pagine/programma-umbria-jazz',
    )

    def parse(self, response):
        for days in response.xpath("//div[@id='accordion']//ul//li"):
            date = days.xpath(".//h1/text()").extract()[0]

            indoor = days.xpath(".//table[1]")
            outdoor = days.xpath(".//table[2]")

            for row in indoor.xpath(".//tr"):
                concert = row.xpath(".//td").extract()
                time = concert[0]
                description = concert[1]

                item = JazzScraperItem()
                item['date'] = "%s %s" % (date, time)
                item['description'] = description
                item['outdoor'] = False
                yield item

            for row in outdoor.xpath(".//tr"):
                concert = row.xpath(".//td").extract()
                if len(concert) == 2:
                    time = concert[0]
                    description = concert[1]

                    item = JazzScraperItem()
                    item['date'] = "%s %s" % (date, time)
                    item['description'] = description
                    item['outdoor'] = True
                    yield item
