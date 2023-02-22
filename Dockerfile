FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

COPY ./app /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
