import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

BASE_URL: str = "http://localhost:1800"


@pytest.fixture(scope="session")
def application():
    from config.initializers import (
        init_app,
        init_routers,
    )
    application: FastAPI = init_app()
    init_routers(application)

    return application


@pytest.fixture(scope="session")
def sync_client(application: FastAPI):
    """
    Синхронный клиент
    """

    sync_client: TestClient = TestClient(app=application, base_url=BASE_URL)
    return sync_client
