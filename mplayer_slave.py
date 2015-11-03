#!/usr/bin/python
# Codec: utf-8
import subprocess
subprocess.call(["mplayer", "-idle", "-slave", "-input", "file=pipe" ])
