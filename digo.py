import os

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.diageo.com/'

list = [
    'https://www.diageo.com/en',
    'https://www.diageo.com/en/our-business',
    'https://www.diageo.com/en/our-business/diageo-at-a-glance',
    'https://www.diageo.com/en/our-business/building-world-class-brands',
    'https://www.diageo.com/en/our-business/our-strategy',
    'https://www.diageo.com/en/our-business/our-business-model',
    'https://www.diageo.com/en/our-business/where-we-operate',
    'https://www.diageo.com/en/our-business/where-we-operate/africa'
]


def get_img_url(img):
    try:
        return (str(img['srcset']), str(img['alt']))
    except Exception as e:
        return ()


def dow_img(bs: BeautifulSoup, base_dir="."):
    imgs = bs.find_all('img')
    for img in imgs:
        img_src = get_img_url(img)
        try:
            if img_src:
                img_url = img_src[0].split(" ")[-2]
                file_name = img_src[1]
                file_url = ''
                file_dir = ''
                if 'https:' in img_url:
                    file_name = img_url.split("/")[-1]
                    file_dir = "/".join(img_url.split("/", 3)[-1].split("/")[0:-1:])
                    file_url = img_url
                elif '?url=' in img_url:
                    file_dir = img_url.split("?")[0]
                    file_suffix = img_url.split("?")[1]
                    file_url = base_url + img_url
                    if not file_name or file_name in '?|><\*&^%$./*!#@!)()__+>?:"':
                        file_name = img_url.split("%2")[-1].split("&")[0]
                    else:
                        file_name = file_name + '.' +file_suffix.split(".")[-1].split("&")[0]
                else:
                    file_dir = "/".join(img_url.split("/")[0:-1:])
                    file_url = base_url + img_url
                    file_name = img_url.split("/")[-1]
                if file_dir:
                    if not os.path.exists(base_dir + "/" + file_dir):
                        os.makedirs(base_dir + "/" + file_dir)
                    img_file = open(base_dir + "/" + file_dir + "/" + file_name, 'wb')
                    img_data = requests.get(file_url)
                    img_file.write(img_data.content)
                    img_file.close()
        except Exception as e:
            print(img_src)
            print(e)


def dow_link_css(bs: BeautifulSoup, base_dir="."):
    links = bs.find_all('link')
    for link in links:
        try:
            link_href = link['href']
            if '.css' in link_href:
                path = base_dir + "/".join(str(link_href).split("/")[0:-1:])
                if not os.path.exists(path):
                    os.makedirs(path)
                css_file = open(base_dir + str(link_href), 'w+', encoding="UTF-8")
                css = requests.get(base_url + link_href)
                css_file.write(css.text)
                css_file.close()
        except Exception as e:
            print(e)


for url in list:
    resp = requests.get(url)

    bs = BeautifulSoup(resp.text)

    dow_img(bs)
    # dow_link_css(bs)
