from abc import abstractmethod
from typing import List

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