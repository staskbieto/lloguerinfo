# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Flat(scrapy.Item):
    date = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    sqft_m2 = scrapy.Field()
    rooms = scrapy.Field()
    bathrooms = scrapy.Field()
    discount = scrapy.Field()
    floor_elevator = scrapy.Field()
    realestate = scrapy.Field()
    realestate_id = scrapy.Field()
    is_new_construction = scrapy.Field()
    conservation_state = scrapy.Field()
    building_type = scrapy.Field()
    building_subtype = scrapy.Field()
    neighb_meanprice = scrapy.Field()
    district_meanprince = scrapy.Field()
