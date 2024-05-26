FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/fastapi_iot

CMD ["fastapi", "run", "fastapi_iot/main.py", "--port", "8000"]