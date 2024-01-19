import uvicorn
from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
import logging

from app.config.config import get_config
from app.db import db

config = get_config()

app = FastAPI(title=config.app_name)

@app.on_event("startup")
async def startup():
    await db.connect_to_database(path=config.database_path, database=config.database_name)
 
@app.on_event("shutdown")
async def shutdown():
    logging.info("Shutting down")
    await db.close_database_connection()

@app.get("/")

#--------#
# Menus #
#--------#

# Fetch the Main Menu Items
@app.get(
    "/get_menu_main/{id_site}"
)
async def get_main_menu(id_site: int): # -> list[Menu_Data]:
    if data_main_menu:
        return data_main_menu
    return JSONResponse(status_code=404, content={"message": "Item not found"})

# Fetch the Links Menu Items
@app.get(
    "/get_menu_links/{id_site}"
)
async def get_menu_links(id_site: int): # -> list[Menu_Data]:
    if data_menu_links:
        return data_menu_links
    return JSONResponse(status_code=404, content={"message": "Item not found"})

#--------#
# Skills #
#--------#

## There is a blockgraph "Badges" block which will utilise the following endpoints,
# e.g. to display the Skills.
# When the blockgraph is created (on load of a page that presents the Skills block), 
# it will fetch the skills and tags.
# It will also include the other Skills endpoints (as strings in the JSON response), 
# so that the block can call them

# Fetch the Skills
# api/items/[x]
@app.get(
    "/get_skills_items/{id_site}",
    # responses={
    #     404: {"model": Site_Details, "description": "The item was not found"}
    # }
)
async def get_skills_items(id_site: int) -> list[Skills_Data]:
    if data_skills:
        return data_skills
    return JSONResponse(status_code=404, content={"message": "Item not found"})

# Update a Skill
@app.post("/update_skill/{id_site}")
def update_skill(id_site: int, body: Skill_Details | dict = dict()):
    return {}

# Add a Skill
# api/items/[x]?skill=[y]
@app.put("/add_skills_item/{id_site}")
def add_skills_item(id_site: int, skill_data: Skill_Details):
    return {}

# Fetch Categories of Skills
@app.get("/get_skills_categories/{id_site}")
async def get_skills_categories(id_site: int) -> list[Skills_Category_Data]:
    if data_skills_tags:
        return data_skills_tags
    return JSONResponse(status_code=404, content={"message": "Item not found"})

# Update a Category of Skills
@app.post("/update_skills_category/{id_site}")
def update_skills_category(id_site: int, skill_category_data: Skill_Category_Details):
    return {}

# Add a Category of Skills
@app.put("/add_skills_category/{id_site}")
def add_skills_category(id_site: int, skill_category_data: Skill_Category_Details):
    return {}

#----------#
# Projects #
#----------#

## There are blockgraph "Card Grid", and "Card Carousel" blocks which will utilise 
# the following endpoints, e.g. to display the Projects.
# When the blockgraph is created (on projects page load), 
# it will fetch the projects cards and categories
# It will also include the other Skills endpoints (as strings in the JSON response), 
# so that the block can call them

# Fetch the Projects
@app.get("/get_projects/{id_site}")
async def get_projects(id_site: int) -> list[Projects_Data]:
    if data_projects:
        return data_projects
    return JSONResponse(status_code=404, content={"message": "Item not found"})

# Update a Project
@app.post("/update_project/{id_site}")
def update_project(id_site: int, id_project: int):
    return {}

# Add a Project
@app.put("/add_project/{id_site}")
def add_project(id_site: int, project: Union[str, None] = None):
    return {}

# Fetch the Categories of Projects
@app.get("/get_projects_categories/{id_site}")
async def get_projects_categories(id_site: int) -> list[Projects_Category_Data]:
    return {}

# Update a Category of Projects
@app.post("/update_projects_category/{id_site}")
def update_projects_category(id_site: int, id_projects_category: int):
    return {}

# Add a Category of Projects
@app.put("/add_projects_category/{id_site}")
def add_projects_category(id_site: int, projects_category: Union[str, None] = None):
    return {}

#-----------#
# BlogPosts #
#-----------#

## There are blockgraph "Blog", and "BlogCarousel" blocks which will utilise 
# the following endpoints, # e.g. to display the blog, and also likewise the research 
# articles, and the courses.
# When the blockgraph is created (on Nlog page load, or Blog preview carousel load), 
# it will fetch the blog posts and categories
# It will also include the other Skills endpoints (as strings in the JSON response), 
# so that the block can call them

# Fetch the Blog Posts
@app.get("/get_blog_posts/{id_site}")
async def get_blog_posts(id_site: int) -> list[Blog_Post_Data]:
    return {}

# Update a Blog Post
@app.post("/update_blog_post/{id_site}")
def update_blog_post(id_site: int, id_blog_post: int):
    return {}

# Add a Blog Post
@app.put("/add_blog_post/{id_site}")
def add_blog_post(id_site: int, blog_post: Union[str, None] = None):
    return {}

# Fetch the Categories of Blog Posts
@app.get("/get_blog_categories/{id_site}")
async def get_blog_categories(id_site: int) -> list[Blog_Post_Category_Data]:
    return {}

# Update a Category of the Blog Posts
@app.post("/update_blog_category/{id_site}")
def update_blog_category(id_site: int, id_blog_category: int):
    return {}

# Add a Category of the Blog Posts
@app.put("/add_blog_category/{id_site}")
def add_blog_category(id_site: int, blog_category: Union[str, None] = None):
    return {}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)