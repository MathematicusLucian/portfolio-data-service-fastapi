# Portfolio Data Service    

>*A lightweight **Python: 3.12** microservice utilising FastAPI, Asyncio, Pydantic, and Motor to fetch data from a MongoDB instance to populate my portfolio Angular website.*

### Features 
- [FastAPI](http://fastapi.tiangolo.com), and **ObjectID**
- **Dependency Injection** features in the database implementation
- Use of Env file to store secrets (parsed by Pydantic)  
- [MongoDB](https://www.mongodb.com) 
- Asynchronous programming (**async**), i.e. Asyncio, for Mongo DB calls
- Dependency manager: [Poetry](https://python-poetry.org) 
- Docker container 

## Launch FastAPI Microservice
### Docker
``sudo docker-compose up``

### Local Machine
``uvicorn main:app --host 0.0.0.0 --port 80``
``uvicorn main:portfolio_data_service --host 0.0.0.0 --port 80``

## Set Python in Path
``python3 -m site --user-base``
``nano ~/.bash_profile``
``xport PATH="/path/to/python:$PATH"``
Ctrl + X -> y -> Enter

## python-dotenv
To open .env files

## Poetry
``poetry init``
``poetry install --no-root`` (To avoid installing development dependencies, use --no-dev argument)

## PyProject (alternate to SetupTools)
### Installing base depdendences
``pip install -e .`` (e=editable: reference rather than copy)
### Installing dev dependencies
``pip install -e .[dev]``
### create EXE file
``renderhtml.exe .\input.md``

## virtualenv (has move features than venv)
### install 
``pip install virtualenv``
``python3> -m venv portfolio-env``
### Launch
env_setup.bash
### Launch: Linux
````source portfolio_env/bin/activate``
### Launch: Windows
``cd portfolio-env``
``Scripts\activate``
### Check virtualenv working / which dependencies are installed
``pip list``
### VSCode Setup
Cmd/Ctrl-Shift-P -> Select Interpreter -> portfolio-service -> env
### Generate requirements file
``pip freeze > requirements.txt``
### Install dependencies (from requirements file)
``(portfolio_env)$ pip install -r requirements.txt``
### Deactivate virtualenv
``(portfolio_env)$ deactivate``

## PipeEnv
``pip3 install --user pipenv``
### pyvenv.cfg
``include-system-site-packages = true``
Then, do ``pip install``

>*Nb. Scripts to be installed in envs are not be written with an expectation that the environment to be activated, and thus, shebang lines contain the absolute paths to their environment’s interpreters.*