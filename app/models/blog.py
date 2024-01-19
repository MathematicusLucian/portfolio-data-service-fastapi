from typing import Optional
from bson import ObjectId
from pydantic.main import BaseModel

from app.models.database import OID, BaseDBModel

class Blog_Post_Data(BaseDBModel):
    id: Optional[OID]
    title: str
    description: str

class Blog_Post_Category_Data(BaseDBModel):
    id: Optional[OID]
    name: str