from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

# Will replace with mongo
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

## There is a blockgraph "Badges" block which will utilise the following endpoints,
# e.g. to display the Skills.
# When the blockgraph is created (on load of a page that presents the Skills block), 
# it will fetch the skills and tags.
# It will also include the other Skills endpoints (as strings in the JSON response), 
# so that the block can call them

# Fetch the Skills
# api/items/[x]
@app.get("/get_skills_items/{id_site}")
def get_skills_items(id_site: int):
    return data_skills

# Update a Skill
@app.post("/update_skill/{id_site}")
def update_skill(id_site: int, id_skill: int):
    return {}

# Add a Skill
# api/items/[x]?skill=[y]
@app.put("/add_skills_item/{id_site}")
def add_skills_item(id_site: int, skill: Skill):
    return {}

# Fetch Categories of Skills
@app.get("/get_skills_categories/{id_site}")
def get_skills_categories(id_site: int):
    return {}

# Update a Category of Skills
@app.post("/update_skills_category/{id_site}")
def update_skills_category(id_site: int, id_skills_category: int):
    return {}

# Add a Category of Skills
@app.put("/add_skills_category/{id_site}")
def add_skills_category(id_site: int, skills_category: Skill_Category):
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
def get_projects(id_site: int):
    return data_projects

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
def get_projects_categories(id_site: int):
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
def get_blog_posts(id_site: int):
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
def get_blog_categories(id_site: int):
    return {}

# Update a Category of the Blog Posts
@app.post("/update_blog_category/{id_site}")
def update_blog_category(id_site: int, id_blog_category: int):
    return {}

# Add a Category of the Blog Posts
@app.put("/add_blog_category/{id_site}")
def add_blog_category(id_site: int, blog_category: Union[str, None] = None):
    return {}