import os , requests
import openpyxl as excel
from bs4 import BeautifulSoup

target_url = 'https://uta.pw/shodou/index.php?master'
save_file = 'meisaku.xlsx'

book = excel.Workbook()
sheet = book.active

html = requests.get(target_url).text
soup = BeautifulSoup(html, 'html5lib')

res = []
for art in soup.select('.article') :
    art_titles = art.select('.art_title')
    if len(art_titles) < 2:
        continue
    title = art_titles[1].text
    src = art.select('img')[0]['src']
    res.append([title,src])

for row in res:
    sheet.append(row)
book.save(save_file)
