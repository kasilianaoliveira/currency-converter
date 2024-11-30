import uvicorn

if __name__ == "__main__":
    config = uvicorn.Config("src.app:app", port=5000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()
