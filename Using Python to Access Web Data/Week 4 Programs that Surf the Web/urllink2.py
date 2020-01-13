'''
Scraping HTML Data with BeautifulSoup
'''
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Sample data: http://py4e-data.dr-chuck.net/comments_42.html
# Actual data: http://py4e-data.dr-chuck.net/comments_355382.html
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
numlist=list()
for tag in tags:
    # Look at the parts of a tag
    numlist.append(int(re.findall('>([0-9]+)<',tag.decode())[0]))
print(sum(numlist))
