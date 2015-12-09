#!/usr/bin/python

def mplayerRunning():
    m = os.system('mplayer -running')
    if m == 'ANS_YES no':
        subprocess.call(["mplayer", "-idle", "-slave", "-input", "file=pipe" ]) #"-ao", "alsa",
    else:
        return()
