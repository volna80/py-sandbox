# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
# url = "http://py4e-data.dr-chuck.net/comments_42.html"
url = "http://py4e-data.dr-chuck.net/comments_350303.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
nums = list()
tags = soup('span')
for tag in tags:
    if tag.attrs['class'][0] == "comments":
        nums.append(int(tag.contents[0]))
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)

print(sum(nums))