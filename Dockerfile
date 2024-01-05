FROM python:alpine3.19

COPY . /app
WORKDIR /app

RUN apk update
RUN apk add firefox

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["main.py"]