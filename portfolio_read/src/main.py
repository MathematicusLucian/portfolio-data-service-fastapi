#-------------
# Main module
#-------------
import logging
# import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from app.config.config import get_config
from app.services.database_manager import database_manager_service
from app.api_v1.api import router as api_router
from base_routers import base_router

config = get_config()

origins = [
    "http://localhost:8000",
    "http://localhost:4200",
    "http://127.0.0.1:8000",
    "http://0.0.0.0:8000",
]

app = FastAPI(title=config.app_name)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="/v1")
app.include_router(base_router, prefix='', tags=["Core"])

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

lambda_handler = Mangum(app, lifespan="off")

# def lambda_handler(event, context):
#     message = 'Hello' # {} {}!'.format(event['first_name'], event['last_name'])  
#     return { 
#         'message' : message
#     }