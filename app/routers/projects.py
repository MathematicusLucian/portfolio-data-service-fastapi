from typing import Union
import json
from fastapi.responses import JSONResponse

from app.models.projects import Projects_Category_Data, Projects_Data

#----------#
# Projects #
#----------#

## There are blockgraph "Card Grid", and "Card Carousel" blocks which will utilise 
# the following endpoints, e.g. to display the Projects.
# When the blockgraph is created (on projects page load), 
# it will fetch the projects cards and categories
# It will also include the other Skills endpoints (as strings in the JSON response), 
# so that the block can call them

# Fetch the Projects
@app.get("/get_projects/{id_site}")
async def get_projects(id_site: int) -> list[Projects_Data]:
    if data_projects:
        return data_projects
    return JSONResponse(status_code=404, content={"message": "Item not found"})

# Update a Project
@app.post("/update_project/{id_site}")
def update_project(id_site: int, id_project: int):
    return {}

# Add a Project
@app.put("/add_project/{id_site}")
def add_project(id_site: int, project: Union[str, None] = None):
    return {}

# Fetch the Categories of Projects
@app.get("/get_projects_categories/{id_site}")
async def get_projects_categories(id_site: int) -> list[Projects_Category_Data]:
    return {}

# Update a Category of Projects
@app.post("/update_projects_category/{id_site}")
def update_projects_category(id_site: int, id_projects_category: int):
    return {}

# Add a Category of Projects
@app.put("/add_projects_category/{id_site}")
def add_projects_category(id_site: int, projects_category: Union[str, None] = None):
    return {}