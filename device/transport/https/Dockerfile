# Image environment
FROM g2inc/oif-python
RUN apk upgrade --update && apk add --no-cache dos2unix && rm /var/cache/apk/*

MAINTAINER Screaming_Bunny

LABEL name="HTTPS Transport Module" \
vendor="OpenC2" \
license="BSD" \
version="2.0" \
description="This is the HTTPS Transport Module container"

ADD requirements.txt /tmp/requirements.txt
ADD docker_dev_start.sh /opt/transport/dev_start.sh

RUN apk add --no-cache openssl

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz


# Copy directories
ADD HTTPS/ /opt/transport/HTTPS

# Set working directory
WORKDIR /opt/transport

# Requirements install
RUN apk update && \
  apk add --no-cache \
  bash \
  openssl && \
  apk add docker && \
  pip3 install -r /tmp/requirements.txt && \
  rm -r /root/.cache && \
  chmod +x /opt/transport/dev_start.sh && \
  chmod +w /opt/transport/HTTPS/certs && \
  dos2unix /opt/transport/dev_start.sh && \
#
# Create certs for flask app, not needed if using own certs
  openssl genrsa -des3 -passout pass:develop -out /opt/transport/HTTPS/certs/server.pass.key 2048 && \
  openssl rsa -passin pass:develop -in /opt/transport/HTTPS/certs/server.pass.key -out /opt/transport/HTTPS/certs/server.key && \
  rm /opt/transport/HTTPS/certs/server.pass.key && \
  openssl req -new -key /opt/transport/HTTPS/certs/server.key -out /opt/transport/HTTPS/certs/server.csr \
    -subj "/C=US/O=flask/OU=Screaming Bunny" && \
  openssl x509 -req -days 365 -in /opt/transport/HTTPS/certs/server.csr -signkey /opt/transport/HTTPS/certs/server.key \
    -out /opt/transport/HTTPS/certs/server.crt && \
#
# Cleanup
apk del tar && \
rm /var/cache/apk/* && \
rm -rf *.tar.gz* /usr/src /root/.gnupg /tmp/*
# Run command when container launches
CMD ["./dev_start.sh"]

