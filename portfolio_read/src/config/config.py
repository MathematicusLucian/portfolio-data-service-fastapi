# import os
from os.path import join, dirname
# import dotenv
from dotenv import load_dotenv, find_dotenv
import boto3
from functools import lru_cache
from pydantic_settings import BaseSettings
# from typing import Annotated

from utils.common_helper import isLocal, getEnvVar

@lru_cache() # Reading a file from disk is usually costly :. cache (do it only once)
def load_config():
    # dotenv_path = join(dirname(__file__), '.env')
    # load_dotenv(dotenv_path)
    # load_dotenv(find_dotenv())

    class Config(BaseSettings):
        APP_NAME: str = "Portfolio Data Read Service - Local"
        PORTFOLIO_DATABASE_PATH: str = getEnvVar("PORTFOLIO_DATABASE_PATH")
        PORTFOLIO_DATABASE_NAME: str = getEnvVar("PORTFOLIO_DATABASE_NAME")
        
    config_obj = Config()
    return config_obj