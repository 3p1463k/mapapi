from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

help_page_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@help_page_router.get("/help")
async def map(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("/general_pages/help_page.html", context)
