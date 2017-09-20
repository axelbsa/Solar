FROM ubuntu:16.04
MAINTAINER Axel Sanner <axelsanner@gmail.com>

# Set locale
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y locales
RUN locale-gen en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y software-properties-common \
    python-pip python-dev libxml2-dev libxslt-dev libffi-dev libz-dev \
    libpq-dev

RUN pip install -U pip
ADD requirements.txt /workdir/requirements.txt
WORKDIR /workdir
RUN pip install gunicorn
RUN pip install -Ur requirements.txt

ADD ./ /workdir/

ENTRYPOINT ["exec gunicorn --threads 1 --workers 32 --timeout 60 --bind 0.0.0.0:9000 --access-logfile - --error-logfile - wsgi"]

