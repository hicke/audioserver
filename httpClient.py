<<<<<<< HEAD
#!/usr/bin/python

import httpconnect

def httpRequest(method, route):
    c = httpconnect.connect()
    response = c.retreive(method, route)
    return response(method, route)
=======
import httplib


def httpRequest(method, route):
    conn = httplib.HTTPConnection('localhost', '5000')
    conn.request(method, route)
    response = conn.getresponse()
>>>>>>> origin/master
