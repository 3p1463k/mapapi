import folium
import pandas as pd
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()


@general_pages_router.get("/")
async def home(request: Request):

    start_coords = (50.65973, 14.04430)
    mymap = folium.Map(location=start_coords, zoom_start=14)

    mymap1 = mymap._repr_html_()
    context = {"request": request, "mymap": mymap1}

    return templates.TemplateResponse("/general_pages/homepage.html", context)
