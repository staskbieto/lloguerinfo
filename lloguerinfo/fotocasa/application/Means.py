import os
from os.path import dirname
import pandas as pd
from fotocasa.model.ParsedFlat import Flat

from web.models import NeighbourhoodMeans
import datetime

class Means():
    @staticmethod
    def readMeansGencat():
        excel = pd.read_excel(os.path.join('./fotocasa/resources/mitjana_anual_lloguer_bcn.xls'))

        # Select neighbourhood mean prices for year 2019
        neighbourhood_meanprices = excel.iloc[18:91, 0:3]

        # Prepare the neighbouhood mean prices dataframe
        neighbourhood_meanprices.columns = ['id_neighbourhood', 'neighbourhood', 'neighb_meanprice']
        neighbourhood_meanprices['neighbourhood'] = neighbourhood_meanprices['neighbourhood'].str.lower().str.strip()
        return neighbourhood_meanprices
