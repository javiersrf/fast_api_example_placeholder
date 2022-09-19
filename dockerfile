FROM python:3.9.14-alpine3.16
COPY . .

COPY requirements.txt /tmp/requirements.txt

RUN python3 -m pip install -r /tmp/requirements.txt
RUN cd app
RUN pwd
RUN ls
WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]