from typing import Union
import json
from bson import ObjectId
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.models.database_models import OID
from app.models.projects_models import Projects_Category_Data, Projects_Data
from app.services.database_manager import DatabaseManagerInterface, get_database

projects_router = APIRouter(prefix='/projects')

#----------#
# Projects #
#----------#

## There are blockgraph "Card Grid", and "Card Carousel" blocks which will utilise 
# the following endpoints, e.g. to display the Projects.
# When the blockgraph is created (on projects page load), 
# it will fetch the projects cards and categories
# It will also include the other Skills endpoints (as strings in the JSON response), 
# so that the block can call them

# # CREATE

# # READ
@projects_router.get("/all")
async def all_projects(database_manager_service: DatabaseManagerInterface = Depends(get_database)): #list[Projects_Data]:
    projects = await database_manager_service.all('projects')
    return projects

@projects_router.get('/read/{id_projects}')
async def one_projects(id_projects: str, database_manager_service: DatabaseManagerInterface = Depends(get_database)):
    projects_categories = await database_manager_service.post(id_projects, 'projects')
    return projects_categories

# # UPDATE

# # DELETE

# CATEGORIES #

# # CREATE

# # READ
@projects_router.get("/all_projects")
async def all_skills_categories(database_manager_service: DatabaseManagerInterface = Depends(get_database)): #list[Projects_Category_Data]:
    categories = await database_manager_service.all('projects_categories')
    return categories

@projects_router.get('/read_projects/{id_skills_categories}')
async def one_skill_category(id_projects: str, database_manager_service: DatabaseManagerInterface = Depends(get_database)):
    category = await database_manager_service.post(id_projects, 'projects_categories')
    return category

# # UPDATE

# # DELETE