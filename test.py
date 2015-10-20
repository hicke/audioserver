#!/usr/bin/python
# Codec: utf-8
#from mplayer import Player, CmdPrefix
import os
import subprocess


#subprocess.call(["mplayer" "-idle", "-slave", "-input file=pipe"])

#arg = "echo \"loadfile 5487272-hi.m4a\" > pipe"
#command = "mplayer -idle -slave -input file=pipe > mlog.txt"

#os.system(arg)
subprocess.call(["mplayer", "-idle", "-slave", "-input", "file=pipe" ]) #"-ao", "alsa", 
