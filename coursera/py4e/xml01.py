import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = "http://py4e-data.dr-chuck.net/comments_42.xml"
url = "http://py4e-data.dr-chuck.net/comments_350305.xml"
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)

counts = tree.findall('.//count')

data = list()
for c in counts:
    data.append(int(c.text))

print("Count:", len(data))
print("Sum:",sum(data))

