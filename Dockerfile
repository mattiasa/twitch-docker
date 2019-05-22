FROM jrottenberg/ffmpeg:4.0

RUN apt-get update && apt-get install -y wget python libssl-dev python-pip && apt-get clean

ADD requirements.txt /

RUN pip install -r /requirements.txt


ADD scripts/* /usr/local/bin/

WORKDIR /videos

ENTRYPOINT []
