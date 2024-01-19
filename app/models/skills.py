from typing import Optional
from bson import ObjectId
from pydantic.main import BaseModel, BaseDBModel

from app.models.database import OID

class Site_Details(BaseDBModel):
    id: Optional[OID]
    name: str

class Skill_Details(BaseDBModel):
    id: Optional[OID]
    skill_name: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id_skill": 1,
                    "skill_name": "ABC"
                }
            ]
        }
    }

class Skills_Data(BaseDBModel):
    id: Optional[OID]
    name: str
    tag: list

class Skill_Category_Details(BaseDBModel):
    id: Optional[OID]
    skills_category_name: str

class Skills_Category_Data(BaseDBModel):
    id: Optional[OID]
    name: str