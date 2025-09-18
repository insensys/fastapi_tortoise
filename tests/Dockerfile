FROM python:3.11-slim

WORKDIR /tests

COPY tests/requirements.txt /tests/requirements.txt

RUN pip install --no-cache-dir -r tests/requirements.txt
COPY tests /tests
COPY src /tests/src

CMD ["sleep", "infinity"]