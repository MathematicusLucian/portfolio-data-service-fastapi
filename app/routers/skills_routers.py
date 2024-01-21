from typing import Union
import json
from fastapi.responses import JSONResponse

from app.models.skills_models import Skill_Category_Details, Skill_Details, Skills_Category_Data, Skills_Data

#--------#
# Skills #
#--------#

## There is a blockgraph "Badges" block which will utilise the following endpoints,
# e.g. to display the Skills.
# When the blockgraph is created (on load of a page that presents the Skills block), 
# it will fetch the skills and tags.
# It will also include the other Skills endpoints (as strings in the JSON response), 
# so that the block can call them

# Fetch the Skills
# api/items/[x]
@app.get(
    "/get_skills_items/{id_site}",
    # responses={
    #     404: {"model": Site_Details, "description": "The item was not found"}
    # }
)
async def get_skills_items(id_site: int) -> list[Skills_Data]:
    if data_skills:
        return data_skills
    return JSONResponse(status_code=404, content={"message": "Item not found"})

# Update a Skill
@app.post("/update_skill/{id_site}")
def update_skill(id_site: int, body: Skill_Details | dict = dict()):
    return {}

# Add a Skill
# api/items/[x]?skill=[y]
@app.put("/add_skills_item/{id_site}")
def add_skills_item(id_site: int, skill_data: Skill_Details):
    return {}

# Fetch Categories of Skills
@app.get("/get_skills_categories/{id_site}")
async def get_skills_categories(id_site: int) -> list[Skills_Category_Data]:
    if data_skills_tags:
        return data_skills_tags
    return JSONResponse(status_code=404, content={"message": "Item not found"})

# Update a Category of Skills
@app.post("/update_skills_category/{id_site}")
def update_skills_category(id_site: int, skill_category_data: Skill_Category_Details):
    return {}

# Add a Category of Skills
@app.put("/add_skills_category/{id_site}")
def add_skills_category(id_site: int, skill_category_data: Skill_Category_Details):
    return {}