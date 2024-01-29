from typing import Optional
from bson import ObjectId
from pydantic.main import BaseModel

from models.database_models import OID, BaseDBModel

class Menu_Data(BaseDBModel):
    id: Optional[OID]
    title: str
    icon: str
    linkPath: str
    target: str 
    active: bool