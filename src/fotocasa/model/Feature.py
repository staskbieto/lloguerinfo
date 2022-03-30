from pydantic import BaseModel


class Feature(BaseModel):
    key: str
    value: int
    maxValue: int
    minValue: int
