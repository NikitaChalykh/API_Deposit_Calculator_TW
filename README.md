REST API service for deposit calculator
=====

Project description
----------
The project is an API service for calculating deposits based on the received data vector.

The project is deployed in a Docker container.

The project is covered with unit tests.

System requirements
----------

* Python 3.11+
* Docker
* Works on Linux

Technology stack
----------

* Python 3.11+
* fastapi 0.103.2
* pytest
* Docker, Docker Compose

Installing the project from the repository
----------
1. Cloning the repository::
```bash
git clone https://github.com/NikitaChalykh/deposit_calculator.git

cd deposit_calculator # Go to the directory with the project
```

2. Create a ```.env``` file using ```env.example``` as a template

3. Installing and running the project in a container:
```bash
docker-compose up -d
```

4. Launching unit tests:
```bash
docker exec -it deposit-calculation-service pytest
```

Project documentation
----------
Documentation for the API (swagger) after installation is available at:

```http://127.0.0.1:8000/docs/```
