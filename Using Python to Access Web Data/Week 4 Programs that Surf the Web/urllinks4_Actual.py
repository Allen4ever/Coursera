'''
Following Links in HTML Using BeautifulSoup
'''
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') # Enter - http://py4e-data.dr-chuck.net/known_by_Caiolea.html

# Retrieve all of the anchor tags
last_name_list=list()
t=0

while t<7:
    url_list=list()
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser') 
    tags = soup('a')
    for tag in tags:
        url_list.append(tag.get('href', None))   
    last_name_list.append(re.findall('known_by_(.+)\.html',url_list[17]))
    # OR last_name_list.append(re.findall('[A-Z][$a-z]+',url_list[2]))
    url=url_list[17]
    t=t+1
    
print(last_name_list[-1])
