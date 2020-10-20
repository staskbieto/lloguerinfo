__author__ = 'Pol Bieto'

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re

from idealista.items import Link


class IdealistaSpider(CrawlSpider):
    name = "idealista_links"
    allowed_domains = ["idealista.com"]
    start_urls = ['https://www.idealista.com/alquiler-viviendas/barcelona-barcelona/mapa']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@id='sublocations']/li")),
             callback='parse_links',
             follow=True),
    )

    def parse_links(self, response):
        if not re.search('map', response.request.url):
            pass

        link = Link()
        link['neighborhood'] = response.xpath('//span[@class="breadcrumb-title icon-arrow-dropdown-after"]/text()').get()
        link['href'] = response.request.url
        yield link
