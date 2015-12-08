#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import json
import os
from httpClient import httpRequest

# Get json from sr.se
response = urllib.urlopen('http://api.sr.se/api/v2/episodes/index?programid=2000&format=json&audioquality=hi&page=1&size=1')
data = json.load(response)

# Extract the correct url from json
url = data['episodes'][0]['broadcast']['broadcastfiles'][0]['url']

# Extract correct filename
soundFile = url.split('/')[-1]

# Open correct url
f = urllib.urlopen(url)

# Check if file exists
if os.path.exists(soundFile):
    print("File exists")
else:
    # Open file and set as binary
    fh = open(soundFile, 'wb')
    # Write binary file to disk
    fh.write(f.read())
    # Close file
    fh.close()
    httpRequest('POST', '/play')

# Todo
#
# Check if Land- or Sjöväder
# If there is a new mp3-file, delete old
# POST to business layer that new file has arrived
# Download image from SR
# "imageurltemplate": "http://sverigesradio.se/sida/images/2000/2877928_512_512.jpg"
# Get title
#  "title": "Land- och sjöväder 20151016 07:55",
