from bs4 import BeautifulSoup

with open('fish.html' ,encoding = 'utf-8') as fp :
    html = fp.read()

soup = BeautifulSoup(html,'html5lib')
for h2 in soup.find_all('h2'):
    if h2.string == 'ウナギ':
        for e in h2.next_siblings :
            if e.name == 'p':
                if e['class'][0] == 'price':
                    print(e.string)

