from fastapi import APIRouter

from .routers import base_routers, blog_routers, menu_routers, projects_routers, skills_routers

router = APIRouter()
router.include_router(base_routers.base_router, prefix='/base', tags=["Core"])
router.include_router(blog_routers.blog_router, prefix='/blog', tags=["Blog"])
router.include_router(menu_routers.menu_router, prefix='/menu_items', tags=["Menu"])
router.include_router(projects_routers.projects_router, prefix='/projects', tags=["Projects"])
router.include_router(skills_routers.skills_router, prefix='/skills', tags=["Skills"])