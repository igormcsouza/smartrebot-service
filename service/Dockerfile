FROM python:3.8

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false

WORKDIR /service
COPY *.lock *.toml /service/
RUN poetry install

COPY . /service

#TODO: Review gunicorn command
CMD gunicorn service.run:app