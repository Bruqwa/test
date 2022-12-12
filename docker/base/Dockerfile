FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV TZ=Etc/UTC

WORKDIR /code
COPY . /code

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && apt update \
    && apt install -y --assume-yes python3-dev libpq-dev build-essential python3-pip \
    && apt install libgeos-dev -y \
    && python3 -m pip install -r requirements/base.txt -r requirements/tests.txt

CMD python3 excel_onfly.py