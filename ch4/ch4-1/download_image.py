import requests

url = 'https://uta.pw/shodou/img/3/3.png'

res = requests.get(url)

if not res.ok :
    print('失敗:', res.status_code)
    quit()

with open('gyudon.png', 'wb')as fp:
    fp.write(res.content)

print("ok.")