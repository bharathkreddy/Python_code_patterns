from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
name = []
cnt = int(input('Enter count - '))
position = int(input('Enter Position - '))-1
for i in range(cnt):
    print(i)
    if i == 0:
        url = url
    else:
        url = url2
    print(url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    url2 = (tags[position].get('href',None))
    name = tags[position].contents[0]
    print(name)

    #print(tag.get('href', None))