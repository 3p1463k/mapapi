from fastapi import APIRouter, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from apis.version1.route_upload import map


import pandas as pd
import folium
import shutil
import os

download_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@download_router.get("/download")
async def map(request: Request):

    context = {"request": request, "map": map}
    return templates.TemplateResponse("/general_pages/download_page.html", context)
