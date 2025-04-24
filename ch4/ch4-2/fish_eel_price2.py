from bs4 import BeautifulSoup

with open('fish.html', encoding = 'utf-8') as fp:
    html = fp.read()

soup = BeautifulSoup(html, 'html5lib')

p = soup.select('div#eel > p.price')
print(p[0].string)