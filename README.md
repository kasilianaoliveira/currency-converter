# Currency Converter API

This project provides an API that allows you to convert one currency to another using the Alpha Vantage API. The service accepts a source currency, target currency, and an amount to convert, returning the converted value with two decimal places.

## Features
- Currency conversion between any two supported currencies.
- Uses the Alpha Vantage API to fetch real-time exchange rates.
- Returns the converted value rounded to two decimal places.

## Technologies Used
- **FastAPI** - A modern, fast (high-performance) web framework for building APIs with Python.
- **aiohttp** - Asynchronous HTTP Client/Server framework for handling API requests.
- **Alpha Vantage API** - API for getting real-time and historical market data (currency exchange rates in this case).
- **Pydantic** - Data validation and settings management.
  
## Prerequisites
Before running the project, ensure you have the following installed:

- Python 3.12+
- `pip` for managing Python packages
- An API key for Alpha Vantage (sign up [here](https://www.alphavantage.co/support/#api-key))

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/currency-converter-api.git
   cd currency-converter-api
   ```

2. Create and activate a virtual environment:



  ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
  ```

3. Install the dependencies:
  ```bash
    pip install -r requirements.txt
  ```

4. Create a .env file in the root directory of the project and add your Alpha Vantage API key:

  ```bash
    ALPHAVANTAGE_API_KEY=your_alpha_vantage_api_key
  ```



## Usage

  1. To run the API locally:
   ```bash
    python main.py
  ```

## Endpoints

  ```bash
    GET /convert
    Converts an amount from one currency to another.

    Parameters
    from_currency: The source currency (e.g., USD).
    to_currency: The target currency (e.g., EUR).
    price: The amount to be converted (float).
  ```

