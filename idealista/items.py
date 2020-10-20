# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IdealistaItem(scrapy.Item):
    date = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    sqft_m2 = scrapy.Field()
    rooms = scrapy.Field()
    discount = scrapy.Field()
    floor_elevator = scrapy.Field()
    realestate = scrapy.Field()


class Link(scrapy.Item):
    href = scrapy.Field()
    neighborhood = scrapy.Field()
