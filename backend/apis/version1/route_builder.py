from fastapi import APIRouter, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import folium
import shutil
import os

builder_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@builder_router.get("/builder")
async def map(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("/general_pages/builder.html", context)


@builder_router.post("/builder")
async def generated(
    request: Request,
    description: str = Form(),
    value: int = Form(),
    lat: float = Form(),
    lon: float = Form(),
    circle_size: int = Form(),
    exampleRadios: str = Form(),
    colorpickr: str = Form(),
    circle_weight: int = Form(),
    zoom: int = Form(),
):
    df = pd.DataFrame(
        {"Lat": lat, "Lon": lon, "Des": description, "Val": value}, index=[0]
    )
    start_coords = (lat, lon)
    mymap = folium.Map(location=start_coords, zoom_start=zoom)

    for coord in df[["Lat", "Lon", "Des", "Val"]].values:

        folium.CircleMarker(
            location=[coord[0], coord[1]],
            radius=circle_size,
            weight=circle_weight,
            fill_color=colorpickr,
            color="#000",
            popup=[coord[2], coord[3]],
        ).add_to(mymap)

    download_generated = mymap.save("static/tmp/files/map.html")

    mymap = mymap._repr_html_()
    context = {"request": request, "mymap": mymap}

    return templates.TemplateResponse("/general_pages/builder.html", context)
