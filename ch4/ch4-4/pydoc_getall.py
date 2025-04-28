import os, requests, urllib, time
import urllib.parse
from bs4 import BeautifulSoup

save_dir = './pydoc_tutorial'
top_page = 'https://docs.python.org/ja/3/tutorial/index.html'
check_url = 'https:/docs.python.org/ja/3/tutorial'

visited = {}

def get_page(url):
    if check_url not in url:
        return
    if url in visited:
        return
    #関数を再起的に呼び出すため訪問管理をきちんとする必要がある
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    html = res.text
    visited[url] = True

    fname = save_dir + "/" + os.path.basename(url)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    with open(fname, 'wb') as f:
        f.write(html.encode('utf-8'))  # ←ここも本当は後述の注意あり
        print('save', fname)

    time.sleep(1)
    soup = BeautifulSoup(html, 'html5lib')
    for a in soup.find_all('a'):
        a_url = urllib.parse.urljoin(url, a.get('href', ''))
        a_url = urllib.parse.urldefrag(a_url)[0]
        get_page(a_url)

if __name__ == '__main__' :
    get_page(top_page)