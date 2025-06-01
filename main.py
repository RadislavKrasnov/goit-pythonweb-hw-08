from fastapi import FastAPI

from src.api import contants, utils

app = FastAPI()

app.include_router(utils.router, prefix="/api")
app.include_router(contants.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
