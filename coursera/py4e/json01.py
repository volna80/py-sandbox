import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = "http://py4e-data.dr-chuck.net/comments_42.json"
url = "http://py4e-data.dr-chuck.net/comments_350306.json"
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
js = json.loads(data.decode())

print(js)

data = list()
for c in js["comments"]:
    data.append(int(c['count']))

print("Count:", len(data))
print("Sum:",sum(data))

