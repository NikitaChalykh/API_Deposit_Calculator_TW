from fastapi import FastAPI


def init_app() -> FastAPI:
    from config import app_config

    app = FastAPI(**app_config)
    return app


def init_routers(application: FastAPI) -> None:
    from config.routers import get_routers

    for router in get_routers():
        application.include_router(router)
