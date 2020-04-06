import requests
from bs4 import BeautifulSoup
import re

countries = ['united_kingdom', 'spain', 'ukraine', 'italy', 'moldova', 'romania', 'russia']


for i in countries:
    r = requests.get('https://en.wikipedia.org/wiki/' + i)
    s = BeautifulSoup(r.text, features='html.parser')

    flag_url = s.find('a', {'href': re.compile(r'^/wiki/File:Flag')}).attrs['href']

    flag_r = requests.get('https://en.wikipedia.org' + flag_url)
    flag_s = BeautifulSoup(flag_r.text, features='html.parser')

    img_link = flag_s.find('a', {'href': re.compile(r'^//upload.wikimedia')}).attrs['href']

    print(img_link)

    img = requests.get('http:' + img_link).content

    with open('E:/Python/cs50/project0/Images/' + i + '.svg', 'wb') as f:
        f.write(img)




