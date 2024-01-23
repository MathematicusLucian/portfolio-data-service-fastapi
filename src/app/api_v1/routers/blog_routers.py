import logging
from fastapi import APIRouter, Depends, Body, Request
from fastapi.responses import JSONResponse
from typing import Union, Any
import json
from bson import ObjectId
from pydantic import BaseModel

from app.models.database_models import OID
from app.models.blog_models import Blog_Post_Category_Data, Blog_Post_Data
from app.services.database_manager import DatabaseManagerInterface, get_database

# class DataItem(BaseModel):
#     id: int | None = None
#     name: str
#     content: str | None = None

blog_router = APIRouter()
collection_name = 'blog'
category_collection_name = 'blog_categories'

#-----------#
# BlogPosts #
#-----------#

## There are blockgraph Blog, and BlogCarousel blocks which will utilise
# the following endpoints, # e.g. to display the blog, and
# also likewise the research articles, and the courses.
# When the blockgraph is created (on Nlog page load, or Blog preview carousel load), 
# it will fetch the blog posts and categories
# It will also include the other Skills endpoints (as strings in the JSON response), 
# so that the block can call them


# class NastyMetaClass(type):
#     pass

# class Foo(metaclass=NastyMetaClass):
#     @classmethod
#     def __get_validators__(cls):
#         yield lambda value: True

class Data_Item(BaseModel):
    name: str | None = None
    content: str | None = None

async def get_body(request: Request):
    return await request.body()

# # CREATE
@blog_router.post("/create", tags=["blog"])
async def foo_body(title: Any = Body(...), 
             content: Any = Body(...), 
             database_manager_service: DatabaseManagerInterface = Depends(get_database)
             ):
    # x = ObjectId()
    body_dict = { 
        # "_id": x,
        "title": title, 
        "content": content 
    }
    post = await database_manager_service.create_item(collection_name, body_dict)
    return post

# @blog_router.post("/create", tags=["blog"])
# # async def create_post(body: bytes = Depends(get_body), database_manager_service: DatabaseManagerInterface = Depends(get_database)):
# async def create_post(
#     item: Any):
#     # database_manager_service: DatabaseManagerInterface = Depends(get_database)):
#     # post = await database_manager_service.create_item(body)
#     # results = item #{"item": item}
#     return item

# READ
@blog_router.get('/all')
async def all_posts(database_manager_service: DatabaseManagerInterface = Depends(get_database)): #list[Blog_Post_Data]:
    posts = await database_manager_service.all(collection_name)
    return posts

@blog_router.get("/of_category/{id_category}")
async def all_post_of_category(id_category: str, database_manager_service: DatabaseManagerInterface = Depends(get_database)): #list[Projects_Data]:
    posts = await database_manager_service.all(collection_name, id_category)
    return posts

@blog_router.get('/read/{identifier_type}/{id_post}')
async def one_post(identifier_type: str, id_post: str, database_manager_service: DatabaseManagerInterface = Depends(get_database)):
    post = await database_manager_service.one_item(identifier_type, id_post, collection_name)
    return post

# # UPDATE
# @blog_router.put("/update/{id_site}")
# async def update_post(post_id: OID, post: Blog_Post_Data, database_manager_service: DatabaseManagerInterface = Depends(get_database)):
#     post = await database_manager_service.update_post(post=post, post_id=post_id)
#     return post

# # DELETE
# @blog_router.delete('/delete/{post_id}')
# async def delete_post(post_id: OID, database_manager_service: DatabaseManagerInterface = Depends(get_database)):
#     await database_manager_service.delete_post(post_id=post_id)

# CATEGORIES #

# # CREATE

# # READ
@blog_router.get("/all_categories")
async def get_blog_categories(database_manager_service: DatabaseManagerInterface = Depends(get_database)): #list[Blog_Post_Category_Data]:
    categories = await database_manager_service.all(category_collection_name)
    return categories

@blog_router.get('/read_categories/{id_categories}')
async def one_blog_category(id_categories: str, database_manager_service: DatabaseManagerInterface = Depends(get_database)):
    post = await database_manager_service.one_item(id_categories, category_collection_name)
    return post

# # UPDATE

# # DELETE