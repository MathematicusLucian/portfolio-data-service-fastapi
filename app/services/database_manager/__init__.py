from app.services.database_manager.interfaces.database_manager_interface import DatabaseManagerService
from app.services.database_manager.impl.mongo_manager import MongoManager

database_manager_service = MongoManager()

async def get_database() -> DatabaseManagerService:
    return database_manager_service