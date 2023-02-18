from uvicorn import run
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World",
            "What is this?": "My first api example with fastAPI"
            }


@app.get('/first_api')
def first_api():
    return "Hello Word I am Programmer"


@app.get("/tell_me_your_name/{name}")
def read_item(name: str):
    return {"Your name is": name}


if __name__ == "__main__":
    run('main:app', host='127.0.0.1', port=8001, reload=True)
