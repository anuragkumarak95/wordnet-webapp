FROM alpine:latest

MAINTAINER Anurag Kumar <anuragkumarak95@gmail.com>

RUN apk --update add --no-cache --virtual w-runtime python3 py3-pip \
    && rm -rf /var/cache/apk/*

COPY requirements.txt /app/requirements.txt
WORKDIR /app/

RUN apk add --no-cache --virtual w-build python3-dev build-base \
    && pip3 install --no-cache-dir -r requirements.txt \
    && rm requirements.txt \
    && apk del w-build \
    && rm -rf /var/cache/apk/*

COPY . /app/

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["run.py"]
