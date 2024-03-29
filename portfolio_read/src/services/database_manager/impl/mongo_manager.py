import logging
from fastapi import Request
from typing import List, Any
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
# from decouple import config

from utils.common_helper import removeFirstHyphen, validate_object_id
from services.database_manager.interfaces.database_manager_interface import DatabaseManagerInterface
from models.blog_models import Blog_Post_Data, Blog_Request_One
from models.database_models import OID
# from app.utils.common_helper import validate_data_retrieved, format_data_to_list

#------------------------------------
# Mongo service:
# Implements DatabaseManagerInterface
#------------------------------------

class MongoManager(DatabaseManagerInterface):
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

    async def connect_to_database(self, path: str, database: str):
        self.client = AsyncIOMotorClient(
            path,
            maxPoolSize=10,
            minPoolSize=10
        )
        try:
            await self.client.admin.command('ping') 
            logging.info("Connection successful.")
        except Exception as e:
            logging.info(f"Log in unsuccessful: {e}")
        self.database = self.client[database] 

    async def close_database_connection(self):
        self.client.close()

    async def create_item(self, collection_name: str, body_data: Any):
        try:
            body_data = body_data.dict()
            await self.database[collection_name].insert_one(body_data)
        except Exception as e:
            logging.info(e)
        return {"message: Success": body_data}

    # async def create_item(self, collection_name: str, body: dict): #Blog_Post_Data):
    #     # for k, v in body.items():
    #         # if k=="id":
    #         #     del body[k]
    #     # body["_id"]=ObjectId
    #     await self.database.items.insert_one(body)
    #     # await self.database[collection_name].insert_one(body.dict(exclude={'id'}))
    #     return body

    # aux: of_category/65add85a5012fb980dc1ec29
    async def all(self, collection_name: str, auxilliary_id: int | None = None): # -> List[Blog_Post_Category_Data]:
        data_list = [] 
        q=""
        try:
            if(auxilliary_id is not None): 
                q={"id_parent": ObjectId(str(auxilliary_id))}
            data_items = self.database[collection_name].find(q)  
        except Exception as e:
            logging.info(f"Log in unsuccessful: {e}")
            return []
        else:
            async for data_item in data_items:
                data_item_list = {}
                for k, data_field in data_item.items():
                    if isinstance(data_field, list):
                        formattedDataItem = []
                        for parentIDItem in data_field:
                            formattedDataItem.append(str(parentIDItem))
                    else:
                        formattedDataItem = str(data_field)
                    data_item_list[removeFirstHyphen(k)] = formattedDataItem
                data_list.append(data_item_list)
            return data_list

    async def one_item(self, identifier_type: str, item_id: str, collection_name: str, auxilliary_id: int | None = None) -> Blog_Request_One: #e.g.: 65a8290874d04214abc99c6c
        try:
            if item_id is not None:
                item_id = validate_object_id(item_id)
                q={'_id': ObjectId(item_id)}
                if(auxilliary_id is not None): q={'_id': ObjectId(item_id), "id_"+identifier_type: auxilliary_id}
                item_q = await self.database[collection_name].find_one(q)
        except Exception as e:
            logging.info(f"Log in unsuccessful: {e}")
            return []
        else:
            if item_q is not None:
                data_item_list = {}
                for k, data_field in item_q.items():
                    data_item_list[removeFirstHyphen(k)] = str(data_field)
                return data_item_list

    # async def update_item(self, item_id: OID, item: Blog_Post_Data):
    #     if item_id & item:
    #         await self.database.items.update_one({'_id': ObjectId(item_id)},
    #             {'$set': item.dict(exclude={'id'})})

    # async def delete_item(self, item_id: OID):
    #     if item_id:
    #         await self.database.items.delete_one({'_id': ObjectId(item_id)})