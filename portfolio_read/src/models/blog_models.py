from typing import Optional
from bson import ObjectId
from pydantic.main import BaseModel

from app.models.database_models import OID, BaseDBModel

class Blog_Request_One(BaseDBModel):
    id: ObjectId

class Blog_Post_Data(BaseDBModel):
    id: str # Optional[OID]
    title: str
    body: str

class Blog_Post_Category_Data(BaseDBModel):
    id: Optional[OID]
    name: str