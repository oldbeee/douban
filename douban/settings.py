# -*- coding: utf-8 -*-

# Scrapy settings for douban project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'doubanm'

SPIDER_MODULES = ['douban.spiders']
NEWSPIDER_MODULE = 'douban.spiders'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'

FEED_URI = u'./douban.csv'#文件保存路径
FEED_FORMAT = 'CSV'#保存为CSV文件
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'douban (+http://www.yourdomain.com)'
