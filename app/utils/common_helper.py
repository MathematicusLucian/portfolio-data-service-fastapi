import logging
from fastapi import HTTPException
from typing import List

from app.models.blog_models import Blog_Post_Data

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