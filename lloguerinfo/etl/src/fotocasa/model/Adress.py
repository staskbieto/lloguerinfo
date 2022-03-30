from typing import Optional

from pydantic import BaseModel


class Address(BaseModel):
    country: str
    customZone: Optional[str]
    district: str
    neighborhood: str
    zipCode: str
    municipality: str
    province: str
    city: str
    cityZone: str
    county: str
    regionLevel1: str
    regionLevel2: str
    upperLevel: str