# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class ProductItem(Item):
    brand = Field()
    title = Field()
    art_no = Field()
    item_url = Field()
    images = Field()
    price = Field()
    image_base_url = Field()
    season = Field()
    week = Field()
    category = Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
