from datetime import date, datetime
from decimal import Decimal

from pydantic import field_validator, BaseModel
from fastapi import HTTPException


class DepositCalculationRequestModel(BaseModel):
    """
    Data query model for deposit calculation.
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
            raise HTTPException(status_code=400, detail="invalid date format in field 'date'")

    @field_validator("periods")
    def parse_periods(cls, value):
        if value < 1 or value > 60:
            raise HTTPException(
                status_code=400,
                detail="Invalid value for field 'periods', must be between 1 and 60",
            )
        return value

    @field_validator("amount")
    def parse_amount(cls, value):
        if value < 10000 or value > 3000000:
            raise HTTPException(
                status_code=400,
                detail="Invalid value for field 'amount', must be between 10000.00 and 3000000.00",
            )
        return value

    @field_validator("rate")
    def parse_rate(cls, value):
        if value < 1 or value > 8:
            raise HTTPException(
                status_code=400,
                detail="Invalid value for field 'rate', must be in range from 1.0 to 8.0",
            )
        return value
