from typing import Optional

from pydantic import BaseModel


class Detail(BaseModel):
    locale: Optional[str]
