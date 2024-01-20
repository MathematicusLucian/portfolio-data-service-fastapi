from app.models.database import OID
from fastapi import APIRouter, Depends
from typing import Union
import json
from fastapi.responses import JSONResponse

from app.models.blog import Blog_Post_Category_Data, Blog_Post_Data
from app.db import DatabaseManager, get_database

router_blog = APIRouter(prefix='/blog')

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
@router_blog.put("/create/{id_site}", tags=["blog"])
async def create_post(id_site: int, blog_post: Union[str, None] = None, db: DatabaseManager = Depends(get_database)) -> list[Blog_Post_Data]:
    post = await db.create_post(id_site, blog_post)
    return post

# READ
@router_blog.get('/all')
async def all_posts(db: DatabaseManager = Depends(get_database)): #list[Blog_Post_Data]:
    posts = await db.all_posts()
    return posts

@router_blog.get('/{id_post}')
async def one_post(id_post: OID, db: DatabaseManager = Depends(get_database)):
    post = await db.get_post(id_post=id_post)
    return post

# UPDATE
@router_blog.put("/update/{id_site}")
async def update_post(post_id: OID, post: Blog_Post_Data, db: DatabaseManager = Depends(get_database)):
    post = await db.update_post(post=post, post_id=post_id)
    return post

# DELETE
@router_blog.delete('/delete/{post_id}')
async def delete_post(post_id: OID, db: DatabaseManager = Depends(get_database)):
    await db.delete_post(post_id=post_id)

# CATEGORIES #

# Fetch the Categories of Blog Posts
@router_blog.get("/get_blog_categories/{id_site}")
async def get_blog_categories(id_site: int) -> list[Blog_Post_Category_Data]:
    return {}

# Update a Category of the Blog Posts
@router_blog.post("/update_blog_category/{id_site}")
def update_blog_category(id_site: int, id_blog_category: int):
    return {}

# Add a Category of the Blog Posts
@router_blog.put("/add_blog_category/{id_site}")
def add_blog_category(id_site: int, blog_category: Union[str, None] = None):
    return {}