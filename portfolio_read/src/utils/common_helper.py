import logging
import os
from fastapi import HTTPException
from typing import List

# from models.blog_models import Blog_Post_Data

def removeFirstHyphen(s: str):
    if (s[0] == "_"):
        return s[1:]
    else: 
        return(s)
    
def toBool(s: str) -> bool:
    truevals = ("yes", "y", "on", "true", "t", "1")
    falsevals = ("no", "n", "off", "false", "f", "0")
    if s.lower() in truevals: 
        return True
    if s.lower() in falsevals: 
        return False
    raise ValueError("Not a boolean")

def isEnvVar(env_var_name: str, default: False) -> bool:
    try:
        env_var = os.environ[env_var_name]
        if env_var is None: 
            return default
        return True
    except KeyError:
        return default

def getEnvVar(env_var_name: str) -> str:
    env_var = "not_found or empty"
    if isEnvVar(env_var_name, False):
        try:
            env_var = os.environ[env_var_name]
            if env_var is None: 
                return "not_found or empty"
            return env_var
        except KeyError:
            return "not_found or empty"

def isLocal() -> bool:
    isEnvVar('AWS_SAM_LOCAL')

def validate_object_id(object_id) -> any:
    if object_id is None:
        logging.info("Status code: 404. ID is invalid")
        raise HTTPException(status_code=404, detail="ID is invalid")   
    return object_id

# def validate_data_retrieved(data_retrieved) -> any:
#     if data_retrieved is None:
#         logging.info("Status code: 404. Requested data does not exist")
#         raise HTTPException(status_code=404, detail="equested data do not exist")   
#     return True

# async def format_data_to_list(data) -> any: # -> list[Blog_Post_Data]:
#     data_list = []   
#     for data_item in data:
#         data_item["id"]=str(data_item["_id"])
#         del[data_item["_id"]]
#         data_list.append(data_item) 
#     return data_list