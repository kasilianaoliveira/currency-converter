from typing import List

from fastapi import APIRouter, HTTPException, Path, Query

from src.models.currrency_models import ConversionResponse
from src.services.currency_service import currency_converter


converter_router = APIRouter()


@converter_router.get(
    "/converter/{from_currency}", response_model=List[ConversionResponse]
)
async def converter(
    from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$"),
    to_currency: str = Query(max_length=100, regex="^[A-Z]{3}(,[A-Z]{3})*$"),
    price: float = Query(gt=0),
):
    to_currencies = to_currency.split(",")
    result = []

    for currency in to_currencies:
        try:
            converted_price = await currency_converter(
                from_currency=from_currency, to_currency=currency, price=price
            )
            result.append(
                ConversionResponse(
                    from_currency=from_currency,
                    to_currency=currency,
                    converted_price=converted_price,
                )
            )
        except HTTPException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)

    return result
