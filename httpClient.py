#!/usr/bin/python

import httpconnect

def httpRequest(method, route):
    c = httpconnect.connect()
    response = c.retreive(method, route)
    return response(method, route)
