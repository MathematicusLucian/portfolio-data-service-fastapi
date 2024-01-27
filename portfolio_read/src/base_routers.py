from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

base_router = APIRouter()
base_router.mount("/static", StaticFiles(directory="static"), name="static")

@base_router.get("/")
# Presents Angular app
def read_root():
    # ng build --base-href static/ --prod
    # with open('static/index.html', 'r') as file_index:
    #     # project/
    #     #     static/
    #     #         index.html
    #     #         ... (files app angular)
    #     #     main.py
    #     html_content = file_index.read()
    return {"lambda": "root"} #HTMLResponse(html_content, status_code=200)