import uvicorn
from decouple import config


if __name__ == "__main__":
    port = config("PORT", default=8000, cast=int)
    config = uvicorn.Config("src.app:app", port=5000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()
