# Portfolio Data Service    

>*A lightweight **Python: 3.12** microservice utilising FastAPI, Asyncio, Pydantic, and Motor to fetch data from a MongoDB instance to populate my portfolio Angular website.*

**Features**

- [FastAPI](http://fastapi.tiangolo.com), and **ObjectID**
- **Dependency Injection** features in the database implementation
- Use of Env file to store secrets (parsed by Pydantic)  
- [MongoDB](https://www.mongodb.com) 
- Asynchronous programming (**async**), i.e. Asyncio, for Mongo DB calls
- Dependency manager: [Poetry](https://python-poetry.org) 
- Docker container 

## Swagger

At ``/docs``

## Unit Tests (Pytest)

``python -m unittest tests/sum_test.py``

## Launch FastAPI Microservice

**Local Machine**

``uvicorn app.main:app --reload --host 0.0.0.0 --port 80``

**AWS Lambda**

Inside your terminal from the root directory of your project, CD into the Python Site Packages folder.

``cd .env/lib/python3.12/site-packages``

Then zip up the contents into the root of the project.

``zip -r9 path/to/root/of/project/function.zip``

CD back into the root of the project.

``cd path/to/root/of/project``

Next we need to add the contents of the app folder so let's add that into the zip file.

``zip -g ./function.zip -r app``

**Docker**

``sudo docker-compose up``

**Create EXE file**

``renderhtml.exe .\input.md``

## Set Python in Path

- ``python3 -m site --user-base``
- ``nano ~/.bash_profile``
- ``xport PATH="/path/to/python:$PATH"``
- Ctrl + X -> y -> Enter

## virtualenv (has move features than venv)

**Install**

- ``pip install virtualenv``

**Create the virtualenv**

- ``virtualenv -p python3.12 env``
<!-- - ``python3> -m venv env`` -->

**Activate the virtualenv**

``env_setup.bash``

### Activate: Linux

````source /env/bin/activate``

### Activate: Windows

``cd env`` (Works on Mac too)

``Scripts\activate``

**Install dependencies**

While in the virtualenv, and from the ``src`` folder/directory:

``pip install -r requirements.txt``

**Check virtualenv working / which dependencies are installed**

``pip list``

**Deactivate the virtualenv**

``(env)$ deactivate``

## VSCode Setup

Cmd/Ctrl-Shift-P -> Select Interpreter -> ``portfolio-service`` -> ``env``

## Dependencies 

**Generate requirements file**

``pip freeze > requirements.txt``

**Install dependencies (from requirements file)**

``(portfolio_env)$ pip install -r requirements.txt``

**PipeEnv**

``pip3 install --user pipenv``

### pyvenv.cfg

``include-system-site-packages = true``

**python-dotenv**

To open .env files

**Poetry**

- ``poetry init``
- ``poetry install --no-root`` (To avoid installing development dependencies, use --no-dev argument)

**PyProject (alternate to SetupTools)**

### Installing base depdendences

``pip install -e .`` (e=editable: reference rather than copy)

### Installing dev dependencies

``pip install -e .[dev]``

>*Nb. Scripts to be installed in envs are not be written with an expectation that the environment to be activated, and thus, shebang lines contain the absolute paths to their environment’s interpreters.*