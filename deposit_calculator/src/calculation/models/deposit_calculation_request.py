from datetime import date, datetime
from decimal import Decimal

from pydantic import field_validator
from fastapi import HTTPException

from ..entities import BasePointsModel


class DepositCalculationRequestModel(BasePointsModel):
    """
    Модель запроса данных для расчета депозита.
    """

    date: str | date
    periods: int
    amount: Decimal
    rate: float

    @field_validator("date")
    def parse_date(cls, value):
        try:
            return datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise HTTPException(status_code=400, detail="Неверный формат даты в поле 'date'")

    @field_validator("periods")
    def parse_periods(cls, value):
        if value < 1 or value > 60:
            raise HTTPException(
                status_code=400,
                detail="Неверное значение поля 'periods', должно быть в диапазоне от 1 до 60",
            )
        return value

    @field_validator("amount")
    def parse_amount(cls, value):
        if value < 10000 or value > 3000000:
            raise HTTPException(
                status_code=400,
                detail="Неверное значение поля 'amount', должно быть в диапазоне от 10000.00 до 3000000.00",
            )
        return value

    @field_validator("rate")
    def parse_rate(cls, value):
        if value < 1 or value > 8:
            raise HTTPException(
                status_code=400,
                detail="Неверное значение поля 'rate', должно быть в диапазоне от 1.0 до 8.0",
            )
        return value
