import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter URL: ')
    if len(address) < 1: break
    uh = urllib.request.urlopen(address, context=ctx)
    data = uh.read().decode()
    js = json.loads(data)
    count = 0
    for item in js["comments"]:
        num = item['count']
        num = int(num)
        count = count + num
    print(count)
