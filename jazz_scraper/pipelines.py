# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import bleach


class ClearText(object):

    def _strip_text(self, string):
        return " ".join(string.split())

    def _strip_html(self, string):
        return bleach.clean(string, strip=True, tags=[])

    def strip(self, string):
        return self._strip_text(self._strip_html(string))

    def process_item(self, item, spider):
        item["date"] = self.strip(item["date"])
        item["description"] = self.strip(item["description"])

        return item
