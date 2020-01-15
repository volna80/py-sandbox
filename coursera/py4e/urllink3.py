# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
url = "http://py4e-data.dr-chuck.net/known_by_Alisdair.html"
pos = 18
count = 7
#<li style="margin-top: 1px;"><a href="http://py4e-data.dr-chuck.net/known_by_Aniqa.html">Aniqa</a></li>

while count > 0:

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('li')
    tag = tags[pos-1]
    print(tag.a.get('href'), tag.a.string)
    url = tag.a.get('href')

    count = count - 1


