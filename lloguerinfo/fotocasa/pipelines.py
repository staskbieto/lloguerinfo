# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from scrapy_djangoitem import DjangoItem
import datetime
from fotocasa.model.ParsedFlat import Flat

import django

from web.models import ExtractionInfo
from web.models import FlatInfo
from web.models import NeighbourhoodMeans
import pandas as pd


class FotocasaPipeline(object):
    extract_info = None
    flats_processed = []

    def open_spider(self, spider):
        django.setup()
        extract_info = ExtractionInfo(
            date=datetime.date.today()
        )
        extract_info.save()
        self.extract_info = extract_info

    def close_spider(self, spider):
        flats_processed_django = [flat.instance for flat in self.flats_processed]
        FlatInfo.objects.bulk_create(flats_processed_django)

        flats_processed_dicts = [dict(flat) for flat in self.flats_processed]
        flats_processed_dicts_datafreme = pd.DataFrame(flats_processed_dicts)
        flats_processed_dicts_datafreme = flats_processed_dicts_datafreme[
            ['price', 'sqft_m2', 'rooms', 'bathrooms', 'discount', 'neighbourhood', 'neighbourhood_id',
             'neighbourhood_meanprice_difference', 'price_m2']]
        flats_processed_dicts_datafreme_mean = flats_processed_dicts_datafreme.groupby(['neighbourhood', 'neighbourhood_id'], as_index=False).mean()
        neighbourhood_means_list = []

        for index, row in flats_processed_dicts_datafreme_mean.iterrows():
            neighbourhood_means_list.append(
                NeighbourhoodMeans(
                    date=datetime.date.today(),
                    price=row['price'],
                    sqft_m2=row['sqft_m2'],
                    rooms=row['rooms'],
                    bathrooms=row['bathrooms'],
                    discount=row['discount'],
                    neighbourhood=row['neighbourhood'],
                    neighbourhood_id=row['neighbourhood_id'],
                    neighbourhood_meanprice_difference=row['price'],
                    price_m2=row['price_m2'],
                    extract_info_id=self.extract_info
                )
            )
        NeighbourhoodMeans.objects.bulk_create(neighbourhood_means_list)

    def process_item(self, item: Flat, spider):
        if item['neighbourhood_meanprice_difference'] is not None:
            item['extract_info_id'] = self.extract_info
            item.save(commit=False)
            self.flats_processed.append(item)
        return item
