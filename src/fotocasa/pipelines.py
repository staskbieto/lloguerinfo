# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xlrd
from itemadapter import ItemAdapter

class IdealistaPipeline(object):
    
    def __get_district_information(self, worksheet):
        districts = [district.lower().strip() for district in worksheet.col_values(1, 7, 17)] 
        district_mean_prices_2019 = worksheet.col_values(2, 7, 17)
        return dict(zip(districts, district_mean_prices_2019))

    def __get_neighbourhood_information(self, worksheet):
        neighbourhoods = [neighbourhood.lower().strip() for neighbourhood in worksheet.col_values(1, 19, 92)]
        neighbourhoods_mean_prices_2019 = worksheet.col_values(2, 7, 92)
        return dict(zip(neighbourhoods, neighbourhoods_mean_prices_2019))

    def open_spider(self, spider):
        workbook = xlrd.open_workbook('mitjana_anual_lloguer_bcn.xls')
        worksheet = workbook.sheet_by_index(0)

        self.districts_mean_price_2019 = self.__get_district_information(worksheet)
        self.neighbourhood_mean_price_2019 = self.__get_neighbourhood_information(worksheet)

    def get_mean_prices(self, address):
        address_components = address.split(',')

        neighbourhood_mean_price = 0
        district_mean_price = 0
        for component in address_components:
            normalized_component = component.lower().strip()
            
            if normalized_component in self.neighbourhood_mean_price_2019.keys():
                neighbourhood_mean_price = self.neighbourhood_mean_price_2019[normalized_component]

            if normalized_component in self.districts_mean_price_2019.keys():
                district_mean_price = self.districts_mean_price_2019[normalized_component]
        
        return neighbourhood_mean_price, district_mean_price

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        adapter['address'] = adapter['address'].lower().trim()

        neighbourhood_mean_price, district_mean_price = self.get_mean_prices(adapter['address'])
        adapter['neighb_meanprice'] = neighbourhood_mean_price
        adapter['district_meanprice'] = district_mean_price
        
        return item
