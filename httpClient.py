import httplib


def httpRequest(method, route):
    conn = httplib.HTTPConnection('localhost', '5000')
    conn.request(method, route)
    response = conn.getresponse()
    #print response.status, response.reason
