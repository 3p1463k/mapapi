from fastapi import APIRouter, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import folium
import shutil

builder_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@builder_router.get("/builder")
async def map(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("/general_pages/builder_page.html", context)


@builder_router.post("/builder")
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

    for coord in df[["Lat", "Lon", "Des", "Val"]].values:

        folium.CircleMarker(
            location=[coord[0], coord[1]],
            radius=30,
            weight=2,
            fill_color="#000",
            color="#000",
            popup=[coord[2], coord[3]],
        ).add_to(mymap)
    mymap1 = mymap._repr_html_()
    context = {"request": request, "mymap": mymap1}

    return templates.TemplateResponse("/general_pages/builder_page.html", context)
