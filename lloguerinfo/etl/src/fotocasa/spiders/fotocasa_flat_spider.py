from scrapy import Request

from fotocasa.application.Mapper import Mapper
from fotocasa.model.FotocasaInfo import FotocasaInfo
from fotocasa.model.ParsedFlat import Flat
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import re
import json


class FotocasaFlatsSpider(CrawlSpider):
    name = "fotocasa_flats"
    allowed_domains = ["fotocasa.es"]

    def start_requests(self):
        urls =  [
        'https://www.fotocasa.es/es/alquiler/viviendas/barcelona-capital/todas-las-zonas/l/{}'.format(i) for i in range(1,200)]
        for url in urls:
            yield Request(url=url, callback=self.parse)

#    rules = (
#        # Filter all the flats paginated by the website following the pattern indicated
#        Rule(LinkExtractor(allow=r"/l/\d*", tags='link'),
#             callback='parse_flats',
#             follow=True),
#    )

    def parse(self, response):
        initData = re.findall('window.__INITIAL_PROPS__ = JSON.parse\((.*)\);', response.text)
        initDataJson = json.loads(json.loads(initData[0]))

        for rawFlat in initDataJson['initialSearch']['result']['realEstates']:
            mapper = Mapper()
            item = mapper.rawFlatToObject(rawFlat)
            yield item