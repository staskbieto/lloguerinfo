from typing import List, Optional, Dict
from uuid import UUID

from pydantic import BaseModel

from fotocasa.model.Adress import Address
from fotocasa.model.Coordinates import Coordinates
from fotocasa.model.Date import Date
from fotocasa.model.DateOriginal import DateOriginal
from fotocasa.model.Detail import Detail
from fotocasa.model.Feature import Feature
from fotocasa.model.Multimedia import Multimedia


class FotocasaInfo(BaseModel):
    accuracy: bool
    address: Address
    buildingSubtype: str
    buildingType: str
    clientAlias: str
    clientId: int
    clientTypeId: int
    clientUrl: Optional[str]
    coordinates: Coordinates
    date: Date
    dateOriginal: DateOriginal
    description: Optional[str]
    detail: Dict
    externalContactUrl: Optional[str]
    features: List[Feature]
    hasVideo: int
    hasVgo: bool
    id: int
    isDiscarded: bool
    isExternalContact: bool
    isFaved: bool
    isHighlighted: bool
    isPackAdvancePriority: bool
    isPackBasicPriority: bool
    isPackMinimalPriority: bool
    isPackPremiumPriority: bool
    isMsAdvance: bool
    isNew: bool
    isNewConstruction: bool
    hasOpenHouse: bool
    isOpportunity: bool
    isTrackedPhone: Optional[str]
    isTop: bool
    isVirtualTour: bool
    location: str
    minPrice: int
    multimedia: List[Multimedia]
    otherFeaturesCount: int
    periodicityId: int
    phone: Optional[str]
    price: Optional[str]
    promotionId: Optional[int]
    promotionLogo: Optional[str]
    promotionUrl: Optional[str]
    promotionTitle: Optional[str]
    promotionTypologiesCounter: Optional[str]
    rawPrice: Optional[int]
    realEstateAdId: Optional[UUID]
    reducedPrice: Optional[str]
    subtypeId: int
    transactionTypeId: int
    typeId: int