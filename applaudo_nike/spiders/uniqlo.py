# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from . import GenericSpider


class UniqloSpider(GenericSpider):
    name = 'uniqlo'
    allowed_domains = ['uniqlo.com']
    custom_settings = dict(
            DOWNLOADER_MIDDLEWARES={
                'applaudo_nike.middlewares.SeleniumDownloaderMiddleware': 543,
            }
    )