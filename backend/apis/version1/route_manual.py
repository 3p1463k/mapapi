from fastapi import APIRouter, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import folium
import shutil

manual_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@manual_router.get("/manual")
async def map(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("/general_pages/create_manualy.html", context)


@manual_router.post("/generated")
async def generated(
    request: Request,
    description: str = Form(),
    value: int = Form(),
    lat: float = Form(),
    lon: float = Form(),
):
    df = pd.DataFrame(
        {"Lat": lat, "Lon": lon, "Des": description, "Val": value}, index=[0]
    )
    start_coords = (lat, lon)
    mymap = folium.Map(location=start_coords, zoom_start=17)
    mymap1 = mymap._repr_html_()
    context = {"request": request, "mymap": mymap1}

    return templates.TemplateResponse("/general_pages/generated.html", context)

    # return {"description": description, "value":value, "lat":lat, "lon":lon}
