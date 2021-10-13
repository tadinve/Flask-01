FROM python:3.8.0-alpine


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add build-base
# install dependencies
RUN pip install --upgrade pip

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]