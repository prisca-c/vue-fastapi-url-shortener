FROM python:3.9

ARG API_PORT

WORKDIR /code

COPY /api/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY /api/app /code/app

ENV API_PORT=${API_PORT}

ENTRYPOINT ["sh", "-c", "fastapi run app/main.py --port ${API_PORT} --reload"]