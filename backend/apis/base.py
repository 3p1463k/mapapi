from fastapi import APIRouter
from apis.version1 import route_homepage
from apis.version1 import route_map
from apis.version1 import route_help_page
from apis.version1 import route_manual
from apis.version1 import route_builder
from apis.version1 import route_download


api_router = APIRouter()

api_router.include_router(
    route_homepage.homepage_router, prefix="", tags=["general_pages"]
)
api_router.include_router(route_map.map_router, prefix="", tags=["map"])

api_router.include_router(route_help_page.help_page_router, prefix="", tags=["map"])

api_router.include_router(route_manual.manual_router, prefix="", tags=["map"])

api_router.include_router(route_builder.builder_router, prefix="", tags=["map"])

api_router.include_router(route_download.download_router, prefix="", tags=["map"])
