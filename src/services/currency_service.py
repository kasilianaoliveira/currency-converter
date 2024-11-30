import aiohttp
from fastapi import HTTPException
from decouple import config

ALPHAVANTAGE_API_KEY = config("ALPHAVANTAGE_API_KEY")


async def currency_converter(from_currency: str, to_currency: str, price: float):
    """
    Converts the given value from one currency to another using the Alpha Vantage API.

    :param from_currency: Source currency
    :param to_currency: Target currency
    :param price: Value to be converted
    :return: Converted Value
    """

    url_api_currency = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_API_KEY}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url_api_currency) as response:
                data = await response.json()
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)

    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=404, detail=f"Currency not found. {data}")

    exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    converted_value = round(price * exchange_rate, 2)
    return converted_value
