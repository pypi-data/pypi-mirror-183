from fastapi import FastAPI, APIRouter
from .test import router as crot_route


def app_route():
    route = APIRouter(prefix="/api")
    route.include_router(crot_route)
    return route


def init_routers(app_: FastAPI) -> None:
    app_.include_router(app_route())
