import os
from fotocasa.model.FotocasaInfo import FotocasaInfo
from fotocasa.model.ParsedFlat import Flat
import re
import datetime
from fotocasa.resources.mapping import fotocasa_gencat_map

from fotocasa.application.Means import Means


class Mapper():
    neighbourhood_meanprices = Means.readMeansGencat()

    # Given a fotocasa address,
    # retrieves the excel neighbourhood name
    def gencat_neighb(self, fotocasa_address):
        fotocasa_address = fotocasa_address.lower()
        for k in fotocasa_gencat_map.keys():
            is_same = re.search(k, fotocasa_address)
            if is_same:
                return fotocasa_gencat_map[k]
        return ""

    def is_valid_field(self, value):
        return value is not None and value > 0

    def loadRentMeans(self, flat: Flat):
        flat['neighbourhood'] = self.gencat_neighb(flat['neighbourhood'])
        gencat_avg_prices = self.neighbourhood_meanprices[
            self.neighbourhood_meanprices.neighbourhood == flat['neighbourhood']]
        flat['neighbourhood_id'] = gencat_avg_prices['id_neighbourhood'].squeeze()
        flat['neighbourhood_meanprice'] = gencat_avg_prices['neighb_meanprice'].squeeze()

        if self.is_valid_field(flat['price']) and self.is_valid_field(flat['sqft_m2'] > 0):
            flat['price_m2'] = flat['price'] / flat['sqft_m2']
        else:
            flat['price_m2'] = None

        if self.is_valid_field(flat['price_m2']) and self.is_valid_field(flat['neighbourhood_meanprice']):
            flat['neighbourhood_meanprice_difference'] = (flat['price_m2'] - flat['neighbourhood_meanprice']) / flat[
                'neighbourhood_meanprice']
        else:
            flat['neighbourhood_meanprice_difference'] = None

        return flat

    def rawFlatToObject(self, rawFlat):
        flat = FotocasaInfo(**rawFlat)
        rooms = self.extractFeature(flat, "rooms", 0)
        bathrooms = self.extractFeature(flat, "bathrooms", 0)
        elevator = self.extractFeature(flat, "elevator", 0)
        surface = self.extractFeature(flat, "surface", 0)
        conservation_state = self.extractFeature(flat, "conservationState", None)

        reduced_price = float(re.sub('\D', '', flat.reducedPrice)) if flat.reducedPrice else 0.0
        item = Flat(
            date=datetime.date.today(),
            link=list(flat.detail.values())[0],
            price=flat.rawPrice,
            address=flat.location,
            discount=reduced_price,
            sqft_m2=surface,
            bathrooms=bathrooms,
            rooms=rooms,
            floor_elevator=elevator,
            realestate=flat.clientAlias,
            realestate_id=flat.clientId,
            is_new_construction=flat.isNewConstruction,
            conservation_state=conservation_state,
            building_type=flat.buildingType,
            building_subtype=flat.buildingSubtype,
            latitude=flat.coordinates.latitude,
            longitude=flat.coordinates.longitude,
            neighbourhood=flat.address.neighborhood
        )
        return self.loadRentMeans(item)

    def extractFeature(self, flat, name, default):
        feature = [feature.value for feature in flat.features if feature.key == name]
        feature = feature[0] if len(feature) else default
        return feature
