from typing import Union
import json
from bson import ObjectId
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.models.database_models import OID
from app.models.blog_models import Blog_Post_Category_Data, Blog_Post_Data
from app.services.database_manager import DatabaseManagerInterface, get_database

menu_router = APIRouter()
collection_name = 'menu_items'

#--------#
# Menus #
#--------#

# # CREATE

# # READ
@menu_router.get("/all")
async def all(database_manager_service: DatabaseManagerInterface = Depends(get_database)):
    menu = await database_manager_service.all(collection_name)
    return menu

@menu_router.get("/of_category/{id_category}")
async def all_skills_of_category(id_category: str, database_manager_service: DatabaseManagerInterface = Depends(get_database)):
    menu = await database_manager_service.all(collection_name, id_category)
    return menu

@menu_router.get('/read/{identifier_type}/{id_menu_item}')
async def one(identifier_type: str, id_menu_item: str, database_manager_service: DatabaseManagerInterface = Depends(get_database)):
    menu_item = await database_manager_service.one_item(identifier_type, id_menu_item, collection_name)
    return menu_item

# # UPDATE

# # DELETE