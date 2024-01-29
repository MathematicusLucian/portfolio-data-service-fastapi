import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from config.config import load_config
from services.database_manager import database_manager_service
from api_v1.api import router as api_router
from base_route import base_router

# load_dotenv() 
config = load_config()

# origins = [
#     "http://localhost:8000",
#     "http://localhost:4200",
#     "http://0.0.0.0:8000",
#     "http://127.0.0.1:3000",
#     "http://127.0.0.1:8000",
#     "http://127.0.0.1:8080",
# ]

app = FastAPI(title=config.APP_NAME)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

logging.basicConfig(level=logging.DEBUG,
  format='%(asctime)s %(name)-12s %(levelname)-8s %(relativeCreated)6d %(threadName)s %(message)s',
  datefmt='%m-%d %H:%M', 
  filename='temp/portfolio-data-service.log',
  filemode='w') 
# logging.getLogger().setLevel(logging.INFO)

app.include_router(api_router, prefix="/v1")
app.include_router(base_router, prefix='', tags=["Core"])

# #Upgrade to lifespan event handler
# @app.on_event("startup")
# async def startup():
#     logging.info("Requesting database setup")
#     logging.debug("THIS IS A DEBUG LOG")
#     await database_manager_service.connect_to_database(path=config.PORTFOLIO_DATABASE_PATH, database=config.PORTFOLIO_DATABASE_NAME)
 
# #Upgrade to lifespan event handler
# @app.on_event("shutdown")
# async def shutdown():
#     logging.info("Shutting down")
#     await database_manager_service.close_database_connection()

handler = Mangum(app, lifespan="off")