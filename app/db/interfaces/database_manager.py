from abc import abstractmethod
from typing import List

from app.models.blog import Blog_Post_Data

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
    async def get_posts(self) -> List[Blog_Post_Data]:
        pass