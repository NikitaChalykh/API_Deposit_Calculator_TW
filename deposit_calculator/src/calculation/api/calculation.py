from fastapi import APIRouter, status

from ..use_cases import DepositCalculationCase
from ..models import DepositCalculationRequestModel

router = APIRouter(prefix="/calculation", tags=["calculation"])


@router.post(
    "/deposit",
    status_code=status.HTTP_200_OK,
)
def deposit_calculation_view(
    payload: DepositCalculationRequestModel,
) -> dict:
    """
    Апи расчета суммы по депозиту.
    """

    deposit_calculation_case: DepositCalculationCase = DepositCalculationCase()
    return deposit_calculation_case(payload=payload)
