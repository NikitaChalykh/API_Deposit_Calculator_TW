# Тесты апи расчета суммы по депозиту


def test_deposit_calculation_200(sync_client):
    response = sync_client.post(
        url="/calculation/deposit",
        json=dict(
            date="31.12.2021",
            periods=7,
            amount=10000.00,
            rate=6,
        ),
    )

    assert response.status_code == 200
    assert response.json() == {
        "31.12.2021": "10050.00",
        "31.01.2022": "10100.25",
        "28.02.2022": "10150.75",
        "31.03.2022": "10201.51",
        "30.04.2022": "10252.51",
        "31.05.2022": "10303.78",
        "30.06.2022": "10355.29"
    }


def test_deposit_calculation_400_by_date(sync_client):
    response = sync_client.post(
        url="/calculation/deposit",
        json=dict(
            date="32.12.2021",
            periods=7,
            amount=10000.00,
            rate=6,
        ),
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "Неверный формат даты в поле 'date'"}


def test_deposit_calculation_400_by_periods(sync_client):
    response = sync_client.post(
        url="/calculation/deposit",
        json=dict(
            date="31.12.2021",
            periods=61,
            amount=10000.00,
            rate=6,
        ),
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "Неверное значение поля 'periods', должно быть в диапазоне от 1 до 60"}


def test_deposit_calculation_400_by_amount(sync_client):
    response = sync_client.post(
        url="/calculation/deposit",
        json=dict(
            date="31.12.2021",
            periods=1,
            amount=5000.00,
            rate=6,
        ),
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Неверное значение поля 'amount', должно быть в диапазоне от 10000.00 до 3000000.00"
    }


def test_deposit_calculation_400_by_rate(sync_client):
    response = sync_client.post(
        url="/calculation/deposit",
        json=dict(
            date="31.12.2021",
            periods=1,
            amount=10000.00,
            rate=10,
        ),
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "Неверное значение поля 'rate', должно быть в диапазоне от 1.0 до 8.0"}


def test_deposit_calculation_422_by_date(sync_client):
    response = sync_client.post(
        url="/calculation/deposit",
        json=dict(
            periods=1,
            amount=10000.00,
            rate=6,
        ),
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"][1] == "date"


def test_deposit_calculation_422_by_periods(sync_client):
    response = sync_client.post(
        url="/calculation/deposit",
        json=dict(
            date="31.12.2021",
            amount=10000.00,
            rate=6,
        ),
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"][1] == "periods"


def test_deposit_calculation_422_by_amount(sync_client):
    response = sync_client.post(
        url="/calculation/deposit",
        json=dict(
            date="31.12.2021",
            periods=7,
            rate=6,
        ),
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"][1] == "amount"


def test_deposit_calculation_422_by_rate(sync_client):
    response = sync_client.post(
        url="/calculation/deposit",
        json=dict(
            date="31.12.2021",
            periods=7,
            amount=10000.00,
        ),
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"][1] == "rate"
