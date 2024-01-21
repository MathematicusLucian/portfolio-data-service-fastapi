#-------------
# Main module
#-------------
import uvicorn
from fastapi import FastAPI
import logging

from app.config.config import get_config
from app.services.database_manager import database_manager_service
from app.routers import base_routers, blog_routers, menu_routers, projects_routers, skills_routers

config = get_config()

app = FastAPI(title=config.app_name)
app.include_router(base_routers.base_router, prefix='/api')
app.include_router(blog_routers.blog_router, prefix='/api')
app.include_router(menu_routers.menu_router, prefix='/api')
app.include_router(projects_routers.projects_router, prefix='/api')
app.include_router(skills_routers.skills_router, prefix='/api')

@app.on_event("startup")
async def startup():
    await database_manager_service.connect_to_database(path=config.database_path, database=config.database_name)
 
@app.on_event("shutdown")
async def shutdown():
    logging.info("Shutting down")
    await database_manager_service.close_database_connection()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)