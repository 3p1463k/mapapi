import folium
import pandas as pd
from core.config import settings
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, Header, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


templates = Jinja2Templates(directory="templates")

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    start_coords = (50.65973, 14.04430)
    mymap = folium.Map(location=start_coords, zoom_start=14)

    mymap1 = mymap._repr_html_()
    context = {"request": request, "mymap": mymap1}
    return templates.TemplateResponse("/general_pages/homepage.html", context)
