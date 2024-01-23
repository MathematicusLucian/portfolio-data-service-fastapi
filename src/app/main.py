#-------------
# Main module
#-------------
import logging
import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from app.config.config import get_config
from app.services.database_manager import database_manager_service
from app.api_v1.api import router as api_router

config = get_config()

app = FastAPI(title=config.app_name)
app.include_router(api_router, prefix="/v1")

handler = Mangum(app)

#Upgrade to lifespan event handler
@app.on_event("startup")
async def startup():
    await database_manager_service.connect_to_database(path=config.database_path, database=config.database_name)
 
#Upgrade to lifespan event handler
@app.on_event("shutdown")
async def shutdown():
    logging.info("Shutting down")
    await database_manager_service.close_database_connection()

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)