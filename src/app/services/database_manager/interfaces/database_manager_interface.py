from abc import abstractmethod
from typing import List

from app.models.blog_models import Blog_Post_Data
from app.models.database_models import OID

class DatabaseManagerInterface(object):
    @property
    def client(self):
        raise NotImplementedError

    @property
    def db(self):
        raise NotImplementedError

    @abstractmethod
    async def connect_to_database(self, path: str, database: str):
        pass

    @abstractmethod
    async def close_database_connection(self):
        pass
    
    # @abstractmethod
    async def create_item(self, item: dict): #Blog_Post_Data):
        pass

    # @abstractmethod
    # async def all(self, collection_name: str): # -> List[Blog_Post_Data]:
    #     pass

    # @abstractmethod
    # async def one_item(self, item_id: str, collection_name: str) -> Blog_Post_Data:
    #     pass

    @abstractmethod
    async def all(self, collection_name: str, auxilliary_id: int | None = None): # -> List[Blog_Post_Data]:
        pass

    @abstractmethod
    async def one_item(self, identifier_type: str, item_id: str, collection_name: str, auxilliary_id: int | None = None) -> Blog_Post_Data:
        pass

    # @abstractmethod
    # async def update_item(self, item_id: OID, item: Blog_Post_Data):
    #     pass

    # @abstractmethod
    # async def delete_item(self, item_id: OID):
    #     pass