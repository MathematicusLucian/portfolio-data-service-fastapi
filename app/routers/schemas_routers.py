# This serves for validation and serialization of the requests and the responses.

from pydantic import BaseModel

class Item(BaseModel):
    id: int