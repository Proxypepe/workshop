ARG python=python:alpine3.18

FROM ${python} as build
WORKDIR /code

COPY requirements.txt .

RUN python3 -m venv /venv
ENV PATH=/venv/bin:$PATH

RUN pip3 install --no-cache-dir --upgrade  -r requirements.txt


FROM ${python}

ENV PATH=/venv/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN addgroup -S python && adduser -S python -G python

RUN mkdir /code && chown python:python /code
WORKDIR /code

COPY --chown=python:python --from=build /venv /venv
COPY --chown=python:python . .

USER 999

CMD ["python3", "src/main.py"]
