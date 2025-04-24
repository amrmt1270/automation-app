import os
from bs4 import BeautifulSoup

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'fish.html')

with open(file_path, encoding='utf-8') as fp:
    html = fp.read()

soup = BeautifulSoup(html, 'html5lib')
print(soup.find('title'))