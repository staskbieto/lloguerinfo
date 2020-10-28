from fotocasa.items import Flat
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime

import json
import re


class FotocasaFlatsSpider(CrawlSpider):
    name = "fotocasa_flats"
    allowed_domains = ["fotocasa.es"]
    start_urls = [
        'https://www.fotocasa.es/es/alquiler/viviendas/barcelona-capital/todas-las-zonas/l?combinedLocationIds=724,9,8,232,376,8019,0,1152,0;724,9,8,232,376,8019,0,1151,0;724,9,8,232,376,8019,0,1150,0;724,9,8,232,376,8019,0,1149,0;724,9,8,232,376,8019,0,1148,0;724,9,8,232,376,8019,0,1147,0;724,9,8,232,376,8019,0,1146,0;724,9,8,232,376,8019,0,1145,0;724,9,8,232,376,8019,0,1144,0;724,9,8,232,376,8019,0,1143,0&gridType=3']

    rules = (
        # Filter all the flats paginated by the website following the pattern indicated
        Rule(LinkExtractor(restrict_xpaths="//a[@class='sui-LinkBasic sui-PaginationBasic-link']"),
             callback='parse_flats',
             follow=True),
    )

    def parse_flats(self, response):
        initData = re.findall('window.__INITIAL_PROPS__ = JSON.parse\((.*)\);', response.text)
        initDataJson = json.loads(json.loads(initData[0]))

        for flat in initDataJson['initialSearch']['result']['realEstates']:
            rooms = [features['value'] for features in flat['features'] if features.get('key') == 'rooms']
            rooms = rooms[0] if len(rooms) else 0

            bathrooms = [features['value'] for features in flat['features'] if features.get('key') == 'bathrooms']
            bathrooms = bathrooms[0] if len(bathrooms) else 0

            elevator = [features['value'] for features in flat['features'] if features.get('key') == 'elevator']
            elevator = elevator[0] if len(elevator) else 0

            surface = [features['value'] for features in flat['features'] if features.get('key') == 'surface']
            surface = surface[0] if len(surface) else 0

            conservation_state = [features['value'] for features in flat['features'] if
                                  features.get('key') == 'conservationState']
            conservation_state = conservation_state[0] if len(conservation_state) else 0

            reduced_price = re.sub('\D', '', flat['reducedPrice']) if flat['reducedPrice'] else 0

            item = Flat(date=datetime.now().strftime('%Y-%m-%d'),
                        link=list(flat['detail'].values())[0],
                        price=flat['rawPrice'],
                        address=flat['location'],
                        discount=reduced_price,
                        sqft_m2=surface,
                        bathrooms=bathrooms,
                        rooms=rooms,
                        floor_elevator=elevator,
                        realestate=flat['clientAlias'],
                        realestate_id=flat['clientId'],
                        is_new_construction=flat['isNewConstruction'],
                        conservation_state=conservation_state,
                        building_type=flat['buildingType'],
                        building_subtype=flat['buildingSubtype']
                        )
            yield item
