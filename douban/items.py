# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
#
# from scrapy.item import Item, Field
#
#
# class DoubanItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     movie_name = Field()
#     # movie_director = Field()
#     # movie_writer = Field()
#     # movie_roles = Field()
#     # movie_language = Field()
#     # movie_date = Field()
#     # movie_long = Field()
#     # movie_description = Field()

from scrapy import Item, Field

class DoubanmovieItem(Item):
    title = Field()
    movieInfo = Field()
    star = Field()
    critical = Field()
    quote = Field()

class DoubanAiqingItem(Item):
    title = Field()
