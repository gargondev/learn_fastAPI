from uvicorn import run
from fastapi import FastAPI
from cars.routers import cars

app = FastAPI()


app.include_router(cars.router)

if __name__ == "__main__":
    run('main:app', host='127.0.0.1', port=8001, reload=True)
