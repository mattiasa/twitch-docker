FROM jrottenberg/ffmpeg:3.3

RUN apt-get update && apt-get install -y wget python python-pip python-lxml python-requests python-beautifulsoup && apt-get clean

ADD requirements.txt /

RUN pip install -r /requirements.txt


ADD scripts/* /usr/local/bin/

WORKDIR /videos

ENTRYPOINT []
