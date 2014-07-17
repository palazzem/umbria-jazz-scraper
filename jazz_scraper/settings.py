# -*- coding: utf-8 -*-

# Scrapy settings for jazz_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'jazz_scraper'

SPIDER_MODULES = ['jazz_scraper.spiders']
NEWSPIDER_MODULE = 'jazz_scraper.spiders'

ITEM_PIPELINES = {
    'jazz_scraper.pipelines.ClearText': 300
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jazz_scraper (+http://www.yourdomain.com)'
