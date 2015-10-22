import httplib

conn = httplib.HTTPConnection('localhost', '5000')
conn.request("POST", "/stop")
response = conn.getresponse()
print response.status, response.reason
