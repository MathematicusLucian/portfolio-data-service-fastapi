import logging
from fastapi import HTTPException

def validate_data_retrieved(data_retrieved) -> any:
    if data_retrieved is None:
        logging.info("Status code: 404. Requested data does not exist")
        raise HTTPException(status_code=404, detail="equested data do not exist")   
    return True

async def format_data_to_list(data) -> any:
    data_list = []   
    async for data_item in data:
        data_item["_id"] = str(data_item["_id"])
        data_list.append(data_item) 
    return data_list