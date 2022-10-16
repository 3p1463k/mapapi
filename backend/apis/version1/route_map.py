from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import folium

# from schemas.users import UserCreate

map_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@map_router.get("/map")
async def map(request: Request):

    start_coords = (50.65973, 14.04430)
    mymap = folium.Map(location=start_coords, zoom_start=18)
    mymap2 = mymap._repr_html_()
    context = {"request": request}

    return templates.TemplateResponse("/general_pages/create_map.html", context)
