from fastapi import APIRouter


API_PREFIX = '/api/v1'


def register_routers(app):
    router = APIRouter(prefix=API_PREFIX)

    app.include_router(router)
    return app
