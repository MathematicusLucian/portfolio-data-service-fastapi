import os
from dotenv import load_dotenv
from functools import lru_cache
from pydantic_settings import BaseSettings

load_dotenv() 

class Config(BaseSettings):
    app_name: str = "Portfolio Data Service"
    database_path: str = os.getenv("PORTFOLIO_DATABASE_PATH")
    database_name: str = os.getenv("PORTFOLIO_DATABASE_NAME")

@lru_cache()
def get_config():
    return Config() 