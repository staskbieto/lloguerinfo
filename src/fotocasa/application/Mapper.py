from fotocasa.model.FotocasaInfo import FotocasaInfo
from fotocasa.model.ParsedFlat import Flat
import re
from datetime import datetime

class Mapper():
    def rawFlatToObject(self, rawFlat):
        flat = FotocasaInfo(**rawFlat)
        rooms = self.extractFeature(flat, "rooms", 0)
        bathrooms = self.extractFeature(flat, "bathrooms", 0)
        elevator = self.extractFeature(flat, "elevator", 0)
        surface = self.extractFeature(flat, "surface", 0)
        conservation_state = self.extractFeature(flat, "conservationState", None)

        reduced_price = re.sub('\D', '', flat.reducedPrice) if flat.reducedPrice else 0
        item = Flat(date=datetime.now().strftime('%Y-%m-%d'),
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
                    longitude=flat.coordinates.longitude
                    )
        return item

    def extractFeature(self, flat, name, default):
        feature = [feature.value for feature in flat.features if feature.key == name]
        feature = feature[0] if len(feature) else default
        return feature
