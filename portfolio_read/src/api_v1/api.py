from fastapi import APIRouter

from api_v1.routers import skills_routes
from api_v1.routers import blog_routes, menu_routes, projects_routes

router = APIRouter()
router.include_router(blog_routes.blog_router, prefix='/blog', tags=["Blog"])
router.include_router(menu_routes.menu_router, prefix='/menu', tags=["Menu"])
router.include_router(projects_routes.projects_router, prefix='/projects', tags=["Projects"])
router.include_router(skills_routes.skills_router, prefix='/skills', tags=["Skills"])