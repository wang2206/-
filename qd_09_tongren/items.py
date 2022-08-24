# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Qd09TongrenItem_01(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    span = scrapy.Field()
    h1 = scrapy.Field()
    text = scrapy.Field()
class Qd09TongrenItem_02(scrapy.Item):
    title = scrapy.Field()
    text = scrapy.Field()
