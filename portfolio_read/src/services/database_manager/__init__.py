from services.database_manager.interfaces.database_manager_interface import DatabaseManagerInterface
from services.database_manager.impl.mongo_manager import MongoManager

database_manager_service = MongoManager()

async def get_database() -> DatabaseManagerInterface:
    return database_manager_service