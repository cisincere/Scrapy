import json
import os
import time
from bs4 import BeautifulSoup

import requests
BASE_PATH = 'C:\\work\\SOFT\\nginx\\html\\写真'
BASE_URL = 'https://foamgirl.net/chinese/page/1'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ga;q=0.6,zh-TW;q=0.5",
    "cache-control": "no-cache",
}

def get_local_foamgirl_uri_list()-> list:
    ir = []
    f = open('./foamgirl_uri_list.list', 'r', encoding="UTF-8")
    for f1 in f.readlines():
        ir.append(f1.strip())
    return ir


def get_local_img_url_list()-> list:
    ir = []
    f = open('./foamgirl_img_uri.list', 'r', encoding="UTF-8")
    for f1 in f.readlines():
        ir.append(json.loads(f1))
    return ir
def load_start_page_id() -> str:
    with open('./page_start.index', 'r', encoding="UTF-8") as f:
        return f.read().strip()
img_url_list = get_local_img_url_list()
foamgirl_uri_list = get_local_foamgirl_uri_list()
pageStart = load_start_page_id()

def check_append(need_ckeck_dict) -> bool:
    global img_url_list
    if need_ckeck_dict not in img_url_list:
        img_url_list.append(need_ckeck_dict)
def get_max_page(bs) -> int:
    pages = bs.find_all('a', {'class': 'page-numbers'})
    maxPage = 1
    for page in pages:
        tmp = page.get_text().strip().rstrip().lstrip()
        if len(tmp) > 0:
            mp = int("".join(filter(str.isdigit, tmp)))
            if maxPage < mp:
                maxPage = mp
    return maxPage

def get_xie_z_list(bs) -> list:
    xie_z_json_list = []
    xie_fm_a_list = bs.find_all('a', {'class': 'meta-title'})
    for fm_a in xie_fm_a_list:
        uri = str(fm_a['href'])
        str_title = fm_a.string.replace("\n", "")
        str_title = "".join(filter(lambda o: len(o.strip())>0, str_title))
        if not os.path.exists(f'{BASE_PATH}\\{str_title}'):
            os.makedirs(f'{BASE_PATH}\\{str_title}')
        xie_z_json_list.append({
            'url': uri,
            'title': str_title,
            'dir': f'{BASE_PATH}\\{str_title}'
        })
    return xie_z_json_list
def get_img_url(bs) -> str:
    img_list = bs.find_all('img',{'class','alignnone'})
    for il in img_list:
        img_uri = str(il['src'])
        yield img_uri
def get_img(path,uri, index):
    headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "Referer": "https://foamgirl.net/",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ga;q=0.6,zh-TW;q=0.5",
    "cache-control": "no-cache",
    }
    data = requests.get(uri, headers=headers)
    f = open(f'{path}\\{index}.jpg', 'wb')
    f.write(data.content)

if __name__ == '__main__':
    try:
        data = requests.get(BASE_URL, headers=headers)
        foamgirl_html = data.text
        bs = BeautifulSoup(foamgirl_html)
        need_range = get_max_page(bs)
        xie_z_json_list = get_xie_z_list(bs)
        for k in range(int(pageStart), need_range + 1):
            star_uri = f'https://foamgirl.net/chinese/page/{k}'
            data = requests.get(star_uri, headers=headers)
            bs = BeautifulSoup(data.text)
            xie_z_json_list = get_xie_z_list(bs)
            kl = 0
            for sz in xie_z_json_list:
                print(kl)
                url = sz.get('url')
                dir = sz.get('dir')
                if url is not None:
                    res = requests.get(url, headers=headers)
                    bs = BeautifulSoup(res.text)
                    img_range = get_max_page(bs)
                    i = 1
                    if url.strip() not in foamgirl_uri_list:
                        print(url)
                        foamgirl_uri_list.append(url.strip())
                        for uri in get_img_url(bs):
                            check_append({
                                'dir': dir,
                                'uri': uri,
                                'baseUri': url,
                                'i': i
                            })
                            # get_img(dir, uri, i)
                            i = i+1
                            # time.sleep(1)
                    else:
                        i = 9
                    time.sleep(3)
                    for ir in range(2, img_range+1):
                        tmp_url = url
                        tmp_url = tmp_url.replace('.html', '')
                        tmp_url = tmp_url + '_'+str(ir)+'.html'
                        if tmp_url.strip() not in foamgirl_uri_list:
                            print(tmp_url)
                            res = requests.get(tmp_url, headers=headers)
                            bs = BeautifulSoup(res.text)
                            img_range = get_max_page(bs)
                            tmp_list_uri = []
                            for uri in get_img_url(bs):
                                # get_img(dir, uri, i)
                                check_append({
                                'dir': dir,
                                'uri': uri,
                                'baseUri': tmp_url,
                                'i': i
                                })
                                i = i+1
                                # time.sleep(4)
                            else:
                                foamgirl_uri_list.append(tmp_url)
                            time.sleep(4)
                        else:
                            i = i + 9 
                    kl = kl + 1 
            pageStart = k
            
    except Exception as e:
        raise e
    finally:
        with open('./foamgirl_img_uri.list', 'w+', encoding="UTF-8") as f:
            for data in img_url_list:
                f.write(f"{json.dumps(data, ensure_ascii=False)}\n")
        with open('./foamgirl_uri_list.list', 'w+', encoding="UTF-8") as f:
            for data in foamgirl_uri_list:
                f.write(f"{data}\n")
        with open('./page_start.index', 'w+', encoding="UTF-8") as f:
                f.write(str(pageStart))