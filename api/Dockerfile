FROM python:3.9-alpine3.20

ARG API_PORT

WORKDIR /api

COPY /api/__init__.py /api/__init__.py
COPY /api/run.py /api/run.py
COPY /api/requirements.txt /api/requirements.txt
COPY /api/alembic.ini /api/alembic.ini
COPY /api/migrations /api/migrations

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY /api/app /api/app

ENV API_PORT=${API_PORT}

ENTRYPOINT ["sh", "-c", "export PYTHONPATH=/api && fastapi run run.py --port ${API_PORT} --reload"]