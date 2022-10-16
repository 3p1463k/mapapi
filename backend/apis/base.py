from fastapi import APIRouter
from apis.version1 import route_homepage
from apis.version1 import route_map


api_router = APIRouter()

api_router.include_router(
    route_homepage.homepage_router, prefix="", tags=["general_pages"]
)
api_router.include_router(route_map.map_router, prefix="", tags=["map"])
