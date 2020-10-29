# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xlrd
from itemadapter import ItemAdapter
import Levenshtein

class FotocasaPipeline(object):
    
    def __get_district_information(self, worksheet):
        districts = [district.lower().strip() for district in worksheet.col_values(1, 7, 17)] 
        district_mean_prices_2019 = worksheet.col_values(2, 7, 17)
        return dict(zip(districts, district_mean_prices_2019))

    def __get_neighbourhood_information(self, worksheet):
        neighbourhoods = [neighbourhood.lower().strip() for neighbourhood in worksheet.col_values(1, 19, 92)]
        neighbourhoods_mean_prices_2019 = worksheet.col_values(2, 19, 92)
        return dict(zip(neighbourhoods, neighbourhoods_mean_prices_2019))

    def __get_string_similarity(self, first, second):
        key = f'{first}_{second}'
        if not (key in self.string_similarities.keys()):
            self.string_similarities[key] = Levenshtein.ratio(first, second)
        
        return self.string_similarities[key]        

    def open_spider(self, spider):
        workbook = xlrd.open_workbook('mitjana_anual_lloguer_bcn.xls')
        worksheet = workbook.sheet_by_index(0)

        self.districts_mean_price_2019 = self.__get_district_information(worksheet)
        self.neighbourhood_mean_price_2019 = self.__get_neighbourhood_information(worksheet)
        self.string_similarities = {}

    def __get_most_similar_element(self, address_component, comparison_elements):
        max_similarity = 0
        max_similarity_item = None

        # Obtain the most similar neighbourhood
        for element in comparison_elements:
            similarity_ratio = self.__get_string_similarity(address_component, element)

            if similarity_ratio > max_similarity:
                max_similarity = similarity_ratio
                max_similarity_item = element
        
        return max_similarity_item, max_similarity

    def get_mean_prices(self, address):
        address_components = address.split(',')

        neighbourhood_mean_price = 0
        district_mean_price = 0

        # If we only have an address component
        # it can be either a street, a neighbourhood or a district.
        if len(address_components) == 1:
            normalized_component = address_components[0].lower().strip()

            # Check the most similar neighbourhood and district
            max_similarity_neighb_item, max_similarity_neighb = self.__get_most_similar_element(normalized_component, 
                self.neighbourhood_mean_price_2019.keys())

            max_similarity_district_item, max_similarity_district = self.__get_most_similar_element(normalized_component, 
                self.districts_mean_price_2019.keys())

            # Only take into account the most similar item
            if max_similarity_neighb >= max_similarity_district and max_similarity_neighb >= 0.75:

                neighbourhood_mean_price = self.neighbourhood_mean_price_2019[max_similarity_neighb_item]
            
            elif max_similarity_district >= 0.75:
                district_mean_price = self.districts_mean_price_2019[max_similarity_district_item]

        elif len(address_components) > 1:
            # In this case, address can be of the form: street, neighbourhood, district
            # or street, neighbourhood, or even neighbourhood, district. Thus,
            # we only need the last two components of it. Note that the first
            # component will never be the district.

            last_component_normalized = address_components[-1].lower().strip()
            
            # Check the most similar neighbourhood and district
            max_similarity_neighb_item, max_similarity_neighb = self.__get_most_similar_element(last_component_normalized, 
                self.neighbourhood_mean_price_2019.keys())

            max_similarity_district_item, max_similarity_district = self.__get_most_similar_element(last_component_normalized, 
                self.districts_mean_price_2019.keys())
            
            # if the last component is more similar to a district
            # it's probably a district and the second last is probably a neighbourhood.
            # Otherwise, it's probably a neighbourhood
            if max_similarity_district > max_similarity_neighb and max_similarity_district >= 0.75:
                district_mean_price = self.districts_mean_price_2019[max_similarity_district_item]

                second_last_component_normalized = address_components[-2].lower().strip()
                
                max_similarity_neighb_item, max_similarity_neighb = self.__get_most_similar_element(second_last_component_normalized, 
                    self.neighbourhood_mean_price_2019.keys())

                if max_similarity_neighb >= 0.75:
                    neighbourhood_mean_price = self.neighbourhood_mean_price_2019[max_similarity_neighb_item]
            elif max_similarity_neighb >= 0.75:
                neighbourhood_mean_price = self.neighbourhood_mean_price_2019[max_similarity_neighb_item]
        
        return neighbourhood_mean_price, district_mean_price

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        adapter['address'] = adapter['address'].lower().strip()

        neighbourhood_mean_price, district_mean_price = self.get_mean_prices(adapter['address'])
        adapter['neighb_meanprice'] = neighbourhood_mean_price
        adapter['district_meanprice'] = district_mean_price
        
        return item
