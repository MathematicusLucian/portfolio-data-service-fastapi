from abc import abstractmethod
from typing import List

from app.models.blog import Blog_Post_Data
from app.models.database import OID

class DatabaseManager(object):
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
    
    @abstractmethod
    async def create_post(self, post: Blog_Post_Data):
        pass

    @abstractmethod
    async def all_posts(self): # -> List[Blog_Post_Data]:
        pass

    @abstractmethod
    async def get_posts(self) -> List[Blog_Post_Data]:
        pass

    @abstractmethod
    async def get_post(self, post_id: OID) -> Blog_Post_Data:
        pass

    @abstractmethod
    async def update_post(self, post_id: OID, post: Blog_Post_Data):
        pass

    @abstractmethod
    async def delete_post(self, post_id: OID):
        pass