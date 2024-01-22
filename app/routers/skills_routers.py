from typing import Union
import json
from bson import ObjectId
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.models.database_models import OID
from app.models.blog_models import Blog_Post_Category_Data, Blog_Post_Data
from app.models.skills_models import Skill_Category_Details, Skill_Details, Skills_Category_Data, Skills_Data
from app.services.database_manager import DatabaseManagerInterface, get_database

skills_router = APIRouter(prefix='/skills')

#--------#
# Skills #
#--------#

## There is a blockgraph "Badges" block which will utilise the following endpoints,
# e.g. to display the Skills.
# When the blockgraph is created (on load of a page that presents the Skills block), 
# it will fetch the skills and tags.
# It will also include the other Skills endpoints (as strings in the JSON response), 
# so that the block can call them

# # CREATE

# # READ
@skills_router.get("/all")
async def all_skills(database_manager_service: DatabaseManagerInterface = Depends(get_database)): #list[Blog_Post_Category_Data]:
    skills = await database_manager_service.all('skills')
    return skills

@skills_router.get('/read/{id_skills}')
async def one_skill(id_skills: str, database_manager_service: DatabaseManagerInterface = Depends(get_database)):
    skill = await database_manager_service.one_item(id_skills, 'skills')
    return skill

# # UPDATE

# # DELETE

# CATEGORIES #

# # CREATE

# # READ
@skills_router.get("/all_categories")
async def all_skills_categories(database_manager_service: DatabaseManagerInterface = Depends(get_database)): #list[Blog_Post_Category_Data]:
    categories = await database_manager_service.all('skills_categories')
    return categories

@skills_router.get('/read_categories/{id_skills_categories}')
async def one_skill_category(id_categories: str, database_manager_service: DatabaseManagerInterface = Depends(get_database)):
    category = await database_manager_service.one_item(id_categories, 'skills_categories')
    return category

# # UPDATE

# # DELETE