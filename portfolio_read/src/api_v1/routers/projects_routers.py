from typing import Union
import json
from bson import ObjectId
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from models.database_models import OID
from models.projects_models import Projects_Category_Data, Projects_Data
from services.database_manager import DatabaseManagerInterface, get_database

projects_router = APIRouter()
collection_name = 'projects'
category_collection_name = 'projects_categories'

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
    projects = await database_manager_service.all(collection_name)
    return projects

@projects_router.get("/of_category/{id_category}")
async def all_projects_of_category(id_category: str, database_manager_service: DatabaseManagerInterface = Depends(get_database)): #list[Projects_Data]:
    projects = await database_manager_service.all(collection_name, id_category)
    return projects

@projects_router.get('/read/{identifier_type}/{id_projects}')
async def one_projects(identifier_type: str, id_projects: str, database_manager_service: DatabaseManagerInterface = Depends(get_database)):
    projects_categories = await database_manager_service.one_item(identifier_type, id_projects, collection_name)
    return projects_categories

# # UPDATE

# # DELETE

# CATEGORIES #

# # CREATE

# # READ
@projects_router.get("/all_categories")
async def all_categories(database_manager_service: DatabaseManagerInterface = Depends(get_database)): #list[Projects_Category_Data]:
    categories = await database_manager_service.all(category_collection_name)
    return categories

@projects_router.get('/read_categories/{id_skills_categories}')
async def one_category(id_projects: str, database_manager_service: DatabaseManagerInterface = Depends(get_database)):
    category = await database_manager_service.one_item(id_projects, category_collection_name)
    return category

# # UPDATE

# # DELETE