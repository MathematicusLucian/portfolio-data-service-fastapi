# Launch FastAPI Microservice on Local Machine
uvicorn main:app --host 0.0.0.0 --port 80

# Poetry
poetry init
poetry install --no-root (To avoid installing development dependencies, use --no-dev argument)

# virtualenv (has move features than venv)
## install 
pip install virtualenv
python3> -m venv portfolio-env
## Launch
env_setup.bash
## Launch: Linux
source portfolio_env/bin/activate
## Launch: Windows
cd portfolio-env
Scripts\activate
## Check virtualenv working
pip list
## VSCode Setup
Cmd/Ctrl-Shift-P -> Select Interpreter -> portfolio-service -> env
## Generate requirements file
pip freeze > requirements.txt
## Install dependencies (from requirements file)
(portfolio_env)$ pip install -r requirements.txt
## Deactivate virtualenv
(portfolio_env)$ deactivate

Nb. Scripts to be installed in envs are not be written with an expectation that the environment to be activated, and thus, shebang lines contain the absolute paths to their environment’s interpreters.

Package           Version
----------------- -------
annotated-types   0.6.0
anyio             4.2.0
distlib           0.3.8
exceptiongroup    1.2.0
fastapi           0.109.0
filelock          3.13.1
idna              3.6
pip               23.3.2
platformdirs      4.1.0
pydantic          2.5.3
pydantic_core     2.14.6
setuptools        69.0.2
sniffio           1.3.0
starlette         0.35.1
typing_extensions 4.9.0
virtualenv        20.25.0
wheel             0.42.0