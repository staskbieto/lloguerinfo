from pydantic import BaseModel


class Date(BaseModel):
    diff: int
    unit: str
