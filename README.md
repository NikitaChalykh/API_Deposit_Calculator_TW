REST API сервис для расчета депозита
=====

Описание проекта
----------

Проект представляет собой API сервис для расчета депозита по полученному вектору данных.

Проект покрыт юнит тестами.

Системные требования
----------

* Python 3.11+
* Docker
* Works on Linux

Стек технологий
----------

* Python 3.11.6
* fastapi 0.103.2
* pytest
* Docker, Docker Compose

Установка проекта из репозитория
----------
1. Клонирование репозитория::
```bash 
git clone https://github.com/NikitaChalykh/deposit_calculator.git

cd deposit_calculator # Переходим в директорию с проектом
```

2. Создайте файл ```.env``` используя ```env.example``` в качестве шаблона

3. Установка и запуск проекта в контейнере:
```bash 
docker-compose up -d
```

4. Запуск юнит-тестов:
```bash 
docker exec -it deposit-calculation-service pytest
```

Документация к проекту
----------
Документация для API (swagger) после установки доступна по адресу: 

```http://127.0.0.1:8000/docs/```
