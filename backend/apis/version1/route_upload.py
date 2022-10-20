from fastapi import APIRouter, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import folium
import shutil

upload_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@upload_router.get("/upload")
async def map(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("/general_pages/upload.html", context)


@upload_router.post("/uploadfiles/")
async def create_upload_file(request: Request, file: UploadFile = File(...)):

    with open(f"static/tmp/files/{file.filename}", "wb") as f:
        shutil.copyfileobj(file.file, f)
        file_name = f"static/tmp/files/" + file.filename

        def extract_dok(dokument):
            df = pd.read_csv(dokument, delimiter=",")
            df.columns = ["Lat", "Lon", "Des", "Val"]
            mymap = folium.Map(location=[df.Lat.mean(), df.Lon.mean()], zoom_start=16)

            for coord in df[["Lat", "Lon", "Des", "Val"]].values:

                folium.CircleMarker(
                    location=[coord[0], coord[1]],
                    radius=1,
                    color="red",
                    popup=["Description:", coord[2], "Value:", coord[3]],
                ).add_to(mymap)

            download_generated = mymap.save("static/tmp/files/map.html")
            return mymap._repr_html_()

        global map

        map = extract_dok(file_name)
        context = {"request": request, "map": map}

    return templates.TemplateResponse("/general_pages/download_page.html", context)
