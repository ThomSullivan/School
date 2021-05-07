import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
xml = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(xml)
lst = tree.findall('.//comment')
counter = 0
for item in lst:
    counter = counter + int(item.find('count').text)
print(counter)
