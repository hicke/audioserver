#!/usr/bin/python

import urllib2
import urllib
import json
import os

response = urllib.urlopen('http://api.sr.se/api/v2/episodes/index?programid=2000&format=json&audioquality=hi&page=1&size=1')
data = json.load(response)
file_url = data['episodes'][0]['downloadpodfile']['url']
file = urllib2.urlopen(file_url)
file_name = file_url.split('/')[-1]

os.system('curl -O %s' %file_url)
