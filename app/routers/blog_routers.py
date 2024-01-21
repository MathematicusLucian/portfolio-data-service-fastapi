from typing import Union
import json
from bson import ObjectId
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.models.database_models import OID
from app.models.blog_models import Blog_Post_Category_Data, Blog_Post_Data
from app.services.database_manager import DatabaseManagerInterface, get_database

# class DataItem(BaseModel):
#     id: int | None = None
#     name: str
#     content: str | None = None

blog_router = APIRouter(prefix='/blog')

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

# CREATE
# @blog_router.put("/create") #/{id_site}") #, tags=["blog"])
# # async def create_post(id_site: int, blog_post: Union[str, None] = None, db: DatabaseManager = Depends(get_database)): #-> list[Blog_Post_Data]:
# async def create_post(item: DataItem, database_manager_service: DatabaseManagerInterface = Depends(get_database)):
#     # sample_id = ObjectId
#     # blog_post = {"id":{sample_id},"title":"abc title","body":"abc body"}
#     # post = await database_manager_service.create_post(id_site, blog_post)
#     # return post
#     return item

# READ
@blog_router.get('/all')
async def all_posts(database_manager_service: DatabaseManagerInterface = Depends(get_database)): #list[Blog_Post_Data]:
    posts = await database_manager_service.all('posts')
    return posts

@blog_router.get('/read/{id_post}')
async def one_post(id_post: str, database_manager_service: DatabaseManagerInterface = Depends(get_database)):
    post = await database_manager_service.one_item(id_post, 'posts')
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
    categories = await database_manager_service.all('blog_catergories')
    return categories

@blog_router.get('/read_categories/{id_post}')
async def one_blog_category(id_categories: str, database_manager_service: DatabaseManagerInterface = Depends(get_database)):
    post = await database_manager_service.post(id_categories, 'blog_catergories')
    return post

# # UPDATE

# # DELETE