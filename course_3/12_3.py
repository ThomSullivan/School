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

url = input('Enter - ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = input('Enter count: ')
position = input('Enter position: ')
count = int(count)
position = int(position)
# Retrieve all of the anchor tags

while count > 0:
    tags = soup('a')
    tagnum = 1
    for tag in tags:
        if position > tagnum:
            tagnum = tagnum + 1
            continue
        elif position == tagnum:
            name = tag.contents[0]
            tag = tag.get('href', None)
            count = count - 1
            html = urllib.request.urlopen(tag, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            print(name)
            break
        else:
            break
