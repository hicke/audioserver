#!/usr/bin/python
# encoding: utf8
# Todo
#
# Check if Land- or Sjöväder
# If there is a new mp3-file, delete old
# POST to business layer that new file has arrived
# Download image from SR


import urllib
import json
import os

response = urllib.urlopen('http://api.sr.se/api/v2/episodes/index?programid=2000&format=json&audioquality=hi&page=1&size=1')
data = json.load(response)

# Retrieve data
title = data['episodes'][0]['downloadpodfile']['title']
imageUrl = data['episodes'][0]['imageurltemplate']
length = data['episodes'][0]['downloadpodfile']['duration']
seaweather = "sjöväder"
new = title.encode("utf8").lower()


#Check if title contains Sjöväder
if seaweather in new:
    print title
else:
    print "Fail"
