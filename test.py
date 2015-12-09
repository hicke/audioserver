#!/usr/bin/python

from os import walk
import os.path

print os.path.splitext('/Users/hicke/audioserver/*.m4a')[1]



#
# pathlist = []
# for (dirpath, dirnames, filenames) in walk('/Users/hicke/audioserver/'):
#     pathlist(filenames)
# print pathlist[:]
