from pydantic import BaseModel


class Multimedia(BaseModel):
    type: str
    src: str
