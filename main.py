from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from "./projects.json" import data_projects
from "./skills.json" import data_skills

app = FastAPI()

@app.get("/")
def read_root():
    return {"testing": "api"}

class Skill(BaseModel):
    name: str

class Skill_Category(BaseModel):
    name: str

#--------#
# Skills #
#--------#

#Fetch the Skills
# api/items/[x]
@app.get("/get_skills_items/{id_site}")
def read_item(id_site: int):
    return data_skills

#Add a Skill
# api/items/[x]?skill=[y]
@app.put("/add_skills_item/{id_site}")
def read_item(id_site: int, skill: Skill):
    return {}

#Fetch the Skill' Categories
@app.get("/get_skills_categories/{id_site}")
def read_item(id_site: int):
    return {}

#Add a Category for the Skills
@app.put("/add_skills_category/{id_site}")
def read_item(id_site: int, skills_category: Skill_Category):
    return {}

#----------#
# Projects #
#----------#

#Fetch the Projects
@app.get("/get_projects/{id_site}")
def read_item(id_site: int):
    return data_projects

#Add a Project
@app.put("/add_project/{id_site}")
def read_item(id_site: int, project: Union[str, None] = None):
    return {}

#Fetch the Projects' Categories
@app.get("/get_projects_categories/{id_site}")
def read_item(id_site: int):
    return {}

#Add a Category for the Projects
@app.put("/add_projects_category/{id_site}")
def read_item(id_site: int, projects_category: Union[str, None] = None):
    return {}

#-----------#
# BlogPosts #
#-----------#

#Fetch the Blog Posts
@app.get("/get_blog_posts/{id_site}")
def read_item(id_site: int):
    return {}

#Add a Blog Post
@app.put("/add_blog_post/{id_site}")
def read_item(id_site: int, blog_post: Union[str, None] = None):
    return {}

#Fetch the Blog Posts' Categories
@app.get("/get_blog_categories/{id_site}")
def read_item(id_site: int):
    return {}

#Add a Category for the Blog Posts
@app.put("/add_blog_category/{id_site}")
def read_item(id_site: int, blog_category: Union[str, None] = None):
    return {}