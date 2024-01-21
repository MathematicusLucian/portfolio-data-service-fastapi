from fastapi import APIRouter

base_router = APIRouter(prefix='/base')

@base_router.get("/")
async def base(): return {}