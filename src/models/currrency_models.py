from pydantic import BaseModel
from typing import List


class ConversionResponse(BaseModel):
    from_currency: str
    to_currency: str
    converted_price: float
