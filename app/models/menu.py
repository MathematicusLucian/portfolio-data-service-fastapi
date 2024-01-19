from typing import Optional
from bson import ObjectId
from pydantic.main import BaseModel

from app.models.database import OID, BaseDBModel

class Menu_Data(BaseDBModel):
    id: Optional[OID]
    title: str
    icon: str
    linkPath: str
    target: str 
    active: bool