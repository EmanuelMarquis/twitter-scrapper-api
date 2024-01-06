FROM python:alpine3.19

ARG DEV_BUILD

# if DEVELOPMENT_BUILD is set, PY_ENV=Production
ENV PY_ENV=${DEV_BUILD:-Production}

# if DEVELOPMENT_BUILD is set, PY_ENV=Development
ENV PY_ENV=${DEV_BUILD:+Development}

COPY . /app
WORKDIR /app

RUN apk update
RUN apk add firefox

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["echo", "$PY_ENV"]

ENTRYPOINT ["python"]
CMD ["main.py"]