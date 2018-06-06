#! /usr/bin/python

import requests
import sys
import lxml
import lxml.html.soupparser
import re
import datetime

from slugify import slugify

url=sys.argv[1]

r = requests.get(url)

root = lxml.html.soupparser.fromstring(r.content, features="html.parser")

title = root.xpath('//meta[@property="og:title"]')
if title:
    title = title[0]

release_date = root.xpath('//meta[@property="og:video:release_date"]')
if release_date:
    release_date = release_date[0]

if release_date:
    release_date = release_date.attrib['content']
else:
    release_date = datetime.datetime.now().strftime("%H-%M-%S")

title = title.attrib['content']
release_date = re.sub('T.*', '', release_date)

print "{}-{}".format(release_date, slugify(title))
