#! /usr/bin/python

import requests
import sys
import lxml
import lxml.html.soupparser
import re
import os
import datetime
from slugify import slugify

import urlparse

twitch_url=sys.argv[1]

client_id = '9avyvoskgvc2bi0uantgyesqgxtj14'

template_url = "https://api.twitch.tv/kraken/videos/v{video_id}"

video_id = os.path.basename(urlparse.urlparse(twitch_url).path)


r = requests.get(template_url.format(video_id=video_id), headers={
    'client-id': client_id,
    'accept': 'application/vnd.twitchtv.v5+json'
})

r.raise_for_status()

response = r.json()

title = response.get('title')
release_date = response.get('recorded_at')

if not title:
    title = "no title"

if not release_date:
    release_date = datetime.datetime.now().strftime("%H-%M-%S")

release_date = re.sub(':', '-', release_date)

print "{}-{}".format(release_date, slugify(title))
