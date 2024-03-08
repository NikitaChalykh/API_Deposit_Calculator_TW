from fastapi import APIRouter


def get_routers() -> list[APIRouter]:
    from src.calculation.api.calculation import router as calculation_router

    routers: list[APIRouter] = list()
    routers.append(calculation_router)

    return routers
