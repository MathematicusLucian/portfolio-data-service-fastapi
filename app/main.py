#-------------
# Main module
#-------------
import uvicorn
from fastapi import FastAPI
import logging

from app.config.config import get_config
from app.db import db
from app.routers import blog

config = get_config()

app = FastAPI(title=config.app_name)
app.include_router(blog.router_blog, prefix='/api')

@app.on_event("startup")
async def startup():
    await db.connect_to_database(path=config.database_path, database=config.database_name)
 
@app.on_event("shutdown")
async def shutdown():
    logging.info("Shutting down")
    await db.close_database_connection()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)