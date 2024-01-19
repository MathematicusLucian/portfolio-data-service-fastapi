from fastapi import APIRouter, Depends
from typing import Union
import json
from fastapi.responses import JSONResponse

from app.models.blog import Blog_Post_Category_Data, Blog_Post_Data
from app.db import DatabaseManager, get_database

router = APIRouter()

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

# Fetch the Blog Posts
@router.get('/get_blog_posts')
async def all_posts(db: DatabaseManager = Depends(get_database)): #-> list[Blog_Post_Data]:
    posts = await db.get_posts()
    return posts

# Update a Blog Post
@router.post("/update_blog_post/{id_site}")
def update_blog_post(id_site: int, id_blog_post: int):
    return {}

# Add a Blog Post
@router.put("/add_blog_post/{id_site}")
def add_blog_post(id_site: int, blog_post: Union[str, None] = None):
    return {}

# Fetch the Categories of Blog Posts
@router.get("/get_blog_categories/{id_site}")
async def get_blog_categories(id_site: int) -> list[Blog_Post_Category_Data]:
    return {}

# Update a Category of the Blog Posts
@router.post("/update_blog_category/{id_site}")
def update_blog_category(id_site: int, id_blog_category: int):
    return {}

# Add a Category of the Blog Posts
@router.put("/add_blog_category/{id_site}")
def add_blog_category(id_site: int, blog_category: Union[str, None] = None):
    return {}