from core.config import settings
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, Header, APIRouter
from fastapi.staticfiles import StaticFiles
from apis.base import api_router


def include_router(app):
    app.include_router(api_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    return app


app = start_application()
