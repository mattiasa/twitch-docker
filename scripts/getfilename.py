#! /usr/bin/python

import requests
import sys
import lxml
import lxml.html.soupparser
import re

from slugify import slugify


url=sys.argv[1]

#print url

r = requests.get(url)

#print r.content

root = lxml.html.soupparser.fromstring(r.content)

title = root.xpath('//meta[@property="og:title"]')
if title:
    title = title[0]

release_date = root.xpath('//meta[@property="og:video:release_date"]')
if release_date:
    release_date = release_date[0]

title = title.attrib['content']
release_date = release_date.attrib['content']
release_date = re.sub('T.*', '', release_date)

print "{}-{}".format(release_date, slugify(title))
