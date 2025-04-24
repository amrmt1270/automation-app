from bs4 import BeautifulSoup
import openpyxl as excel


with open('fish.html', encoding = "utf-8") as fp:
    html = fp.read()

save_file = 'fish.xlsx'

def write_list__to_excel(ls, save_file):
    book = excel.Workbook()
    sheet = book.active
    for i in range(len(ls)):
        sheet.append(ls[i])
    book.save(save_file)

soup = BeautifulSoup(html, 'html5lib')
res = []
div_list = soup.select('#fishes >div')
for div in div_list:
    fish = div.h2.text
    desc = div.select('.desc')[0].text
    price = div.select('.price')[0].text
    print(fish, desc, price)
    res.append([fish,desc,price])

if __name__ =='__main__' :
    write_list__to_excel(res, save_file)