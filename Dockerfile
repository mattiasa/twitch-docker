FROM mattiasa/ffmpeg:snapshot-ubuntu

RUN apt-get update && apt-get install -y wget python libssl-dev python-pip && apt-get clean

ADD requirements.txt /

RUN pip install -r /requirements.txt

# Ugly hack because of https://github.com/streamlink/streamlink/issues/2680#issuecomment-552024753
RUN sed -i -e 's,pwkzresl8kj2rdj6g7bvxl9ys1wly3j,kimne78kx3ncx6brgo4mv6wki5h1ko,' /usr/local/lib/python2.7/dist-packages/streamlink/plugins/twitch.py

ADD scripts/* /usr/local/bin/


WORKDIR /videos

ENTRYPOINT []
