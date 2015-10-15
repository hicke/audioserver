#!/usr/bin/python

import urllib
import json
import os

# Get json from sr.se
response = urllib.urlopen('http://api.sr.se/api/v2/episodes/index?programid=2000&format=json&audioquality=hi&page=1&size=1')
data = json.load(response)

# Extract the correct url from json
url = data['episodes'][0]['downloadpodfile']['url']

# Extract correct filename
mp3 = url.split('/')[-1]

# Open correct url
f = urllib.urlopen(url)

# Check if file exists
if os.path.exists(mp3):
    print("File exists")
else:
    # Open file and set as binary
    fh = open(mp3, 'wb')
    # Write binary file to disk
    fh.write(f.read())
    # Close file
    fh.close()