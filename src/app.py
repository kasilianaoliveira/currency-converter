from fastapi import FastAPI
from src.controllers.currency_controller import converter_router

app = FastAPI()
app.include_router(converter_router)
