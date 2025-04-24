import os, sys, requests, urllib, time
from bs4 import BeautifulSoup

target_url = 'https://uta.pw//shodou/index.php?master'
save_dir = './image-meisaku'

def download_image():
    html = requests.get(target_url).text
    urls = get_image_urls(html)
    go_download(urls)

def get_image_urls(html):
    soup = BeautifulSoup(html, 'html5lib')
    res = []
    for img in soup.find_all('img'):
        src = img['src']
        url = urllib.parse.urljoin(target_url, src)
        print('img.src =', url)
        res.append(url)
    return res

def go_download(urls):
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    for url in urls :
        fname = os.path.basename(url)
        save_file = save_dir + '/' + fname
        r = requests.get(url)
        with open (save_file, 'wb') as fp :
            fp.write(r.content)
            print('save :', save_file)
        time.sleep(1)

if __name__ == '__main__' :
    download_image()