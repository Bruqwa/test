import pytest
from asgi_lifespan import LifespanManager
from services.rest_api.main import factory
from async_asgi_testclient import TestClient


@pytest.fixture
async def app():
    instance = factory()
    async with LifespanManager(instance):
        yield instance


@pytest.fixture
async def client(app):
    async with TestClient(app) as client:
        yield client
