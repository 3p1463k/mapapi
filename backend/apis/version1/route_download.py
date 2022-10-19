from fastapi import APIRouter, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import folium
import shutil
import os

download_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@download_router.get("/download")
async def map(request: Request):
    mymap1 = "static/files/map.html"
    context = {"request": request, "mymap": mymap1}
    return templates.TemplateResponse("/general_pages/download_page.html", context)
