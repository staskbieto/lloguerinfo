from pydantic import BaseModel


class DateOriginal(BaseModel):
    diff: int
    unit: str
    timestamp: int
