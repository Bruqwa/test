from fastapi import APIRouter
from . import excel


API_PREFIX = '/api/v1'


def register_routers(app):
    router = APIRouter(prefix=API_PREFIX)

    router.include_router(excel.router)

    app.include_router(router)
    return app
