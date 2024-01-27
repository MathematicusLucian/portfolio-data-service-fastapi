import json
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

# from config.config import get_config
from services.database_manager import database_manager_service
from api_v1.api import router as api_router
from base_routers import base_router

# config = get_config()
origins = [
    "http://localhost:8000",
    "http://localhost:4200",
    "http://0.0.0.0:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8080",
]

app = FastAPI()
# app = FastAPI(title=config.app_name)
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
    await database_manager_service.connect_to_database(path=PORTFOLIO_DATABASE_PATH, database=PORTFOLIO_DATABASE_NAME)
 
#Upgrade to lifespan event handler
@app.on_event("shutdown")
async def shutdown():
    logging.info("Shutting down")
    await database_manager_service.close_database_connection()

handler = Mangum(app, lifespan="off")

# def lambda_handler(event, context):
#     """Sample pure Lambda function

#     Parameters
#     ----------
#     event: dict, required
#         API Gateway Lambda Proxy Input Format

#         Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

#     context: object, required
#         Lambda Context runtime methods and attributes

#         Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

#     Returns
#     ------
#     API Gateway Lambda Proxy Output Format: dict

#         Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
#     """

#     return {
#         "statusCode": 200,
#         "body": json.dumps(
#             {
#                 "message": "hello world",
#             }
#         ),
#     }
