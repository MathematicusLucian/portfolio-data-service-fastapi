from typing import Union
import json
from fastapi.responses import JSONResponse

#--------#
# Menus #
#--------#

# Fetch the Main Menu Items
@app.get(
    "/get_menu_main/{id_site}"
)
async def get_main_menu(id_site: int): # -> list[Menu_Data]:
    if data_main_menu:
        return data_main_menu
    return JSONResponse(status_code=404, content={"message": "Item not found"})

# Fetch the Links Menu Items
@app.get(
    "/get_menu_links/{id_site}"
)
async def get_menu_links(id_site: int): # -> list[Menu_Data]:
    if data_menu_links:
        return data_menu_links
    return JSONResponse(status_code=404, content={"message": "Item not found"})