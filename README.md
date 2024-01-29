# Portfolio Data Service    

>*A lightweight **Python: 3.12** microservice utilising FastAPI, Asyncio, Pydantic, and Motor to fetch data from a MongoDB instance to populate my portfolio Angular website.*

## Features

- [FastAPI](http://fastapi.tiangolo.com) (as alternate to Flask), and **ObjectID**
- **Dependency Injection** features in the database implementation
- Use of Env file to store secrets (parsed by **Pydantic**)  
- [MongoDB](https://www.mongodb.com) 
- AWS secrets for secure database credentials
- Asynchronous programming (**async**), i.e. **Asyncio**, for **Mongo DB** calls
- Dependency manager: [Poetry](https://python-poetry.org) 
- **Docker** container deployed to **AWS Lambda**
- **Swagger**: At ``/docs``

## Launch FastAPI Microservice

### Local Machine - Uvicorn

``uvicorn app.main:app --reload --host 0.0.0.0 --port 80``

### Local Machine - SAM

``sam build --user-container && sam local start-api -n .env.json --skip-pull-image -p 8080``

Debugging:

``sam build --user-container && sam local start-api -n .env.json --skip-pull-image -p 5858``

### AWS Lambda

For Lambda functions that use the Python runtime, a dependency can be any Python package or module. When you deploy your function using a .zip archive, you can either add these dependencies to your .zip file with your function code or use a Lambda layer. A layer is a separate .zip file that can contain additional code and other content. 

**Project Approach**

`` sam local start-api -t template.yaml --skip-pull-image -p 8080 ``

Inside your terminal from the root directory of your project, CD into the Python Site Packages folder.

``cd .env/lib/python3.12/site-packages``

Then zip up the contents into the root of the project.

``zip -r9 path/to/root/of/project/function.zip``

``zip -g ./function.zip -r app``

CD back into the root of the project.

``cd path/to/root/of/project``

To install dependencies for the Lambda:

``pip install --target ./package -r src/requirements.txt``

Next we need to add the contents of the app folder so let's add that into the zip file.

``zip -r ../deployment_package.zip .``

Add the lambda_function.py file to the root of the .zip file

``cd ..``
``zip my_deployment_package.zip lambda_function.py``

**Docker**

``sudo docker-compose up``

### Create EXE file

``renderhtml.exe .\input.md``

### Set Python in Path

- ``python3 -m site --user-base``
- ``nano ~/.bash_profile``
- ``xport PATH="/path/to/python:$PATH"``
- Ctrl + X -> y -> Enter

## Secrets (Credentials Management)

To import a .env when building locally with SAM Api (start-api):

``sam build --user-container && sam local start-api -n .env.json --skip-pull-image -p 8080``

With respect to production, a .env, or .secrets, file will not be visible to the AWS Lambda, unless we upload it to the AWS repo. The credentials would be visible in the AWS UI Console once the lambda function is deployed, and the env variables baked into the code at deployment. There is a risk someone will accidentally commit a decrypted .secrets file. Moreover, if more than one repo relies on this database, there would be duplication of this file. Also, there is the issue of where does one then store the password used to decrypt the secrets, i.e. this does not really solve the issue. Likewise, a SSM encrypted env variable via serverless.yml is not ideal. 

Therefore, I am adapting this to use KMS for prod.

## Unit Tests (Pytest)

![automate automate automate](./assets/sb.webp)

``python -m unittest tests/sum_test.py``

## virtualenv (has move features than venv)

**Install the VirtualEnv**

``pip install virtualenv``

**Create the VirtualEnv**

``virtualenv -p python3.12 env``
<!-- - ``python3> -m venv env`` -->

**Activate the VirtualEnv**

``env_setup.bash``

***Activate on Linux***

``source /env/bin/activate``

***Activate on Windows***

``cd env`` (Works on Mac too)

``Scripts\activate``

**Install dependencies**

While in the virtualenv, and from the ``src`` folder/directory:

``pip install -r requirements.txt``

>*Nb. Scripts to be installed in envs are not be written with an expectation that the environment is to be activated, and thus, shebang lines contain the absolute paths to their environment’s interpreters.*

**Check VirtualEnv working / which dependencies are installed**

``pip list``

**Deactivate the VirtualEnv**

``(env)$ deactivate``

**VSCode VirtualEnv Setup**

Cmd/Ctrl-Shift-P 

-> Select Interpreter 

-> ``portfolio-service`` 

-> ``env``

## Dependencies 

**Generate Requirements.txt file**

``pip freeze > requirements.txt``

**Install dependencies (from requirements file)**

``(portfolio_env)$ pip install -r requirements.txt``

### PipeEnv

``pip3 install --user pipenv``

### pyvenv.cfg

``include-system-site-packages = true``

**python-dotenv**

To open .env files

### Poetry

- ``poetry init``
- ``poetry install --no-root`` (To avoid installing development dependencies, use --no-dev argument)

### PyProject (alternate to SetupTools)

**Installing base depdendences**

``pip install -e .`` (e=editable: reference rather than copy)

**Installing dev dependencies**

``pip install -e .[dev]``