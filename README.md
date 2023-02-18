# fast_api_learning_notes :snake:

Notepad for make API with fastApi

## Install FAST API

I do like installing using [poetry](https://python-poetry.org/), like this [way](https://github.com/heldeveloper/tools_python#-referencias-sobre-o-tema).

`poetry init` Start Project.
`poetry shell` Start virtualenv.
`poetry add fastapi` Install Fast Api
`poetry add uvicorn` Install uvicorn we need ASGI server.

If you want to create requirements from poetry, use this command.
`poetry export -f requirements.txt -o requirements.txt`



## How to build professional projects.
Many times we see tutorials, teaching basic projects, but in real life, we do not create projects like these tutorials.
In documentation fast api we found this [article](https://fastapi.tiangolo.com/tutorial/bigger-applications/), which shows how we can create applications using file structure like this.

```shell
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py
```
In fast api doc they brief, this structure would be the equivalent of [Flask's Blueprints](https://flask.palletsprojects.com/en/2.2.x/blueprints/).


## First code api example with fastAPI.

```python
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
```

## Start App
Run the server use [like documentation](https://fastapi.tiangolo.com/#run-it).

You can start with this command.

`uvicorn main:app --reload`

Some other way by main.py like this.

```python
if __name__ == "__main__":
    run('main:app', host='127.0.0.1', port=8001, reload=True)
```