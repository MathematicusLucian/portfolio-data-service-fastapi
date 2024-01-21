import logging
from typing import List
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
# from decouple import config

from app.models.database_models import OID
from app.utils.common_helper import validate_object_id
from app.services.database_manager.interfaces.database_manager_interface import DatabaseManagerService
from app.models.blog_models import Blog_Post_Data, Blog_Request_One
# from app.utils.common_helper import validate_data_retrieved, format_data_to_list

class MongoManager(DatabaseManagerService):
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

    async def create_post(self, post: str): #Blog_Post_Data):
        await self.database.posts.insert_one(post.dict(exclude={'id'}))

    async def all_posts(self): # -> list[Blog_Post_Data]:
        data_list = [] 
        posts_data = self.database.posts.find()  
        async for data_item in posts_data:
            data_item["id"] = str(data_item["_id"])
            del[data_item["_id"]]
            data_list.append(data_item) 
            # data_list = await format_data_to_list(posts_data) 
            return data_list

    async def one_post(self, post_id: str) -> Blog_Request_One: #e.g.: 65a8290874d04214abc99c6c
        if post_id:
            post_id = validate_object_id(post_id)
            post_q = await self.database.posts.find_one({'_id': ObjectId(post_id)})
            if post_q:
                return Blog_Post_Data(**post_q, id=str(post_q['_id']))

    async def update_post(self, post_id: OID, post: Blog_Post_Data):
        if post_id & post:
            await self.database.posts.update_one({'_id': ObjectId(post_id)},
                {'$set': post.dict(exclude={'id'})})

    async def delete_post(self, post_id: OID):
        if post_id:
            await self.database.posts.delete_one({'_id': ObjectId(post_id)})