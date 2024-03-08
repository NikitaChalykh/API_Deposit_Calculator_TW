REST API для калькулятора депозита
=====

Описание проекта
----------
Проект состоит из проектируемого API сервиса для расчета депозита по полученному вектору данных.

API сервис реализуется на базе фреймворка fastapi. Проект покрыт юнит тестами.

Системные требования
----------

* Python 3.11+
* Docker
* Works on Linux, Windows, macOS, BS

Стек технологий
----------

* Python 3.11.6
* fastapi 0.103.2
* pytest
* Docker

Установка проекта из репозитория (Linux и macOS)
----------
1. Клонировать репозиторий и перейти в него в командной строке:
```bash 
git clone https://github.com/NikitaChalykh/deposit_calculator.git

cd deposit_calculator
```

2. Cоздать и открыть файл ```.env``` с переменными окружения:
```bash 
touch .env
```

3. Заполнить ```.env``` файл с переменными окружения по примеру:
```bash 
echo APP_VERSION=1.0 >> .env

echo APP_NAME=deposit-calculation-service >> .env

echo SITE_HOST=0.0.0.0 >> .env
echo SITE_PORT=8000 >> .env

echo SITE_LOG_LEVEL=info >> .env

echo SITE_RELOAD=True >> .env

echo SITE_RELOAD_DELAY=0.25 >> .env

echo DEBUG=True >> .env
```

4. Установка и запуск приложения в контейнерах:
```bash 
docker-compose up -d
```

Документация к проекту
----------
Документация для API (swagger) после установки доступна по адресу: 

```http://127.0.0.1:8000/docs/```
