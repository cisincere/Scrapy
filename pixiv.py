import json
import os
import time

import requests

BASE_URL = 'https://www.pixiv.net/ajax/illust/'

def load_img_id() -> list:
    result = []
    with open('./img_id.index', 'r', encoding="UTF-8") as f:
        for line in f.readlines():
            result.append(line.strip())
    return result


def load_update_id() -> str:
    with open('./update.index', 'r', encoding="UTF-8") as f:
        return f.read().strip()


img_id = load_img_id()
update_id = load_update_id()
need_update_img_id = update_id

def parse_tag(tags: list, tagTranslation: dict) -> []:
    result = []
    for tag in tags:
        result.append(tag)
        translation = tagTranslation.get(tag, {})
        for lang, value in translation.items():
            if value and len(value) > 0:
                result.append(value)
    return result


def dow_img(url, user_id, id, name, suffix):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br",
        "referer": "https://www.pixiv.net/",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ga;q=0.6,zh-TW;q=0.5",
        "cache-control": "no-cache",
    }
    if not os.path.exists(f'C:\\work\\SOFT\\nginx\\html\\img\\{user_id}\\{id}'):
        os.makedirs(f'C:\\work\\SOFT\\nginx\\html\\img\\{user_id}\\{id}')

    img_file = open(f'C:\\work\\SOFT\\nginx\\html\\img\\{user_id}\\{id}\\{name}.{suffix}', 'wb')
    img_data = requests.get(url, headers=headers)
    img_file.write(img_data.content)


img_list = []
img_error_url = []
not_sup_file_name = ['/', '\\', '<', '>', ':', '"', '|', '*', '?']
p = 1
old_id = ''
log = open('./pixiv.log', 'a+', encoding="UTF-8")


def replace_not_sup_file_name(title: str) -> str:
    for item in not_sup_file_name:
        title = title.replace(item, '~')
    return title
def check_ids(ids: list) -> bool:
    global img_id
    for id in ids:
        if str(id) not in img_id:
            return True
    return False
flag = True
def get_pixiv_img():
    global img_list
    global img_id
    global old_id
    global p
    global log
    global img_error_url
    global flag
    global need_update_img_id
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ga;q=0.6,zh-TW;q=0.5",
        "cache-control": "no-cache",
        "Referer": "https://www.pixiv.net/",
        "X-User-Id": "32081625",
        "Sec-Ch-Ua": """\"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114\"""",
        "cookie": """first_visit_datetime_pc=2023-04-19+12%3A41%3A05; p_ab_id=6; p_ab_id_2=7; p_ab_d_id=256691513; yuid_b=NQGZJDM; __utmz=235335808.1681875668.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _fbp=fb.1.1681875668722.1254211920; c_type=28; privacy_policy_notification=0; a_type=0; b_type=2; __utmc=235335808; PHPSESSID=32081625_oDf3J1tYppgDzLksIbuhW3QbYJj6z5DP; device_token=6fe5af4106efc7860f6fb03079221931; _ga_MZ1NL4PHH0=GS1.1.1687664407.2.1.1687664464.0.0.0; _im_vid=01H3RA8M2SEAASFS5K0J366T7Y; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=female=1^6=user_id=32081625=1^9=p_ab_id=6=1^10=p_ab_id_2=7=1^11=lang=zh=1; _gcl_au=1.1.89918381.1688451800; _im_uid.3929=i.JoPPTYAVTxCfj7OIt78jCw; _gid=GA1.2.348992510.1688693120; _ga=GA1.1.114644716.1681875668; tag_view_ranking=Lt-oEicbBr~RTJMXD26Ak~LJo91uBPz4~jH0uD88V6F~fg8EOt4owo~uW5495Nhg-~Ie2c51_4Sp~65aiw_5Y72~tgP8r-gOe_~eVxus64GZU~b_rY80S-DW~zyKU3Q5L4C~pzzjRSV6ZO~5oPIfUbtd6~nQRrj5c6w_~K8esoIs2eW~EUwzYuPRbU~LtW-gO6CmS~DpO7Lofslr~qtVr8SCFs5~RybylJRnhJ~d2oWv_4U1L~YRDwjaiLZn~28gdfFXlY7~kMjNs0GHNN~NBK37t_oSE~B9VsvJr9Z4~pYlUxeIoeg~L58xyNakWW~f4V1aCLsyM~I5npEODuUW~HBlflqJjBZ~kGYw4gQ11Z~q303ip6Ui5~Sjwi7bh6-s~yjXuOIRb29~nktHt4eKXE~BtXd1-LPRH~Mt2C8GjPNp~b1s-xqez0Y~_EOd7bsGyl~y3NlVImyly~SoxapNkN85~PTyxATIsK0~jPsOGzt9Dh~9bexjBsjKX~6rYZ-6JKHq~6RcLf9BQ-w~Xyw8zvsyR4~KOnmT1ndWG~tIqkVZurKP~1yIPTg75Rl~j3leh4reoN~Bd2L9ZBE8q~-StjcwdYwv~QaiOjmwQnI~Bs22qPIxHA~TUVB-oxjcR~Ged1jLxcdL~KYZac79H5v~KwjO9A0Kl6~cryvQ5p2Tx~RBqBcZh7ix~eK9vnMvjjT~ay54Q_G6oX~Ed_W9RQRe_~KexWqtgzW1~KN7uxuR89w~zXUuIJGfCn~XDEWeW9f9i~_pwIgrV8TB~3SAZKPd9Ah~BQFWWhxtER~-qP3pM5H97~PGh9Qwfchx~mqf4KYn6Dx~rGIDVSTFJU~vzxes78G4k~Itu6dbmwxu~RDlnuThmlw~GF09UjQt_e~r1vRjXa1Om~eAg20hju2a~faHcYIP1U0~azESOjmQSV~XBN4bu0mwC~CkDjyRo6Vc~i_dZaon0j6~cGOUnaqaqs~JckS4u3gtG~6vJsaqmMfp~YorCZBoRIF~7lt5DImm6I~4kEIVWXVvI~NdmWnfpI31~CMH7y9clRf~3snGskaBem~lxfrUKMf9f~VMq-Vxsw8k~dk8nf4PK7G; privacy_policy_agreement=6; cto_bundle=7tOY5V9ERUJteExadzB2Rm5CMkRiUmdXWGRhZnN3dkVmdkZSY05SMUllaDIzNU9wUkptWGdkQTU4ajcyVmZ0b2lNWkNwSVpLNkYwZUlUS2x1OVRWTE5FYXh2WlQlMkJmbXlEZjNieVVrb2JTZ0VZTUx0SXlJZzlDdmhtZklvYU95eG1JVGdjSm0lMkZLR3E3bGpUVjA2VnFyTyUyQjM3WXclM0QlM0Q; __utma=235335808.114644716.1681875668.1688693071.1688696142.25; __cf_bm=GBDLBQsppwDWBW0pkZl_3pGws3CdU7neNj2BpLQUyo4-1688696143-0-AeyJx1mHKnVb1hkyo4XwujTZc8AE1RzUTiXd40r+gyXwmfeeCr0T5LqND3YhuGN7VHiAbTFnZm6hjpRMIp0cyt4ntw5URqOE1nd/RyjtHKU21LtplOKyk9UofN06R+FLWg==; __utmt=1; __utmb=235335808.1.10.1688696142; _ga_75BBYNYN9J=GS1.1.1688696139.28.1.1688696196.0.0.0"""
    }
    result = requests.get(f'https://www.pixiv.net/ajax/follow_latest/illust?p={p}&mode=all&lang=zh', headers=headers)
    log.write(f'https://www.pixiv.net/ajax/follow_latest/illust?p={p}&mode=all&lang=zh\n')
    pixiv_json = json.loads(result.text)
    log.write(f"{json.dumps(pixiv_json, ensure_ascii=False)}\n")
    if not pixiv_json.get('error', True):
        body = pixiv_json.get('body', {})
        ids = pixiv_json.get('body', {}).get('page', {}).get('ids', [''])
        need_scrapy_imag = check_ids(ids)
        if not need_scrapy_imag:
            time.sleep(4)
        if need_scrapy_imag:
            tagTranslation = body.get('tagTranslation')
            thumbnails = body.get('thumbnails', {})
            illust_list = thumbnails.get('illust', [])
            for illust in illust_list:
                title = illust.get('title', 'Rinko')
                id = illust.get('id', '0315')
                userId = illust.get('userId', 'Rinko')
                userName = illust.get('userName', 'Rinko')
                tags = ",".join(parse_tag(illust.get('tags', []), tagTranslation))
                if len(id) > 0 and id not in img_id:
                    illust_result = requests.get(BASE_URL + id + '/pages', headers=headers)
                    pixiv_illust_json = json.loads(illust_result.text)
                    if not pixiv_illust_json.get('error', True):
                        illust_body = pixiv_illust_json.get('body', [])
                        for index, ib in enumerate(illust_body):
                            if p == 1 and index == 0:
                                need_update_img_id =id
                            url = ib.get('urls', {}).get('original', '')
                            try:
                                dow_img(url, userId, id, replace_not_sup_file_name(title) + '_' + str(index),
                                        url.split(".")[-1])
                                img_id.append(id)
                                img_list.append({
                                    'title': title,
                                    'save_title': replace_not_sup_file_name(title),
                                    'id': id,
                                    'userId': userId,
                                    'userName': userName,
                                    'tags': tags,
                                    'url': url
                                })
                                print("id:", id, " dow OK !")
                                time.sleep(4)
                            except Exception as e:
                                time.sleep(2)
                                dow_img(url, userId, id, replace_not_sup_file_name(title) + '_' + str(index),
                                        url.split(".")[-1])
                                img_id.append(id)
                                img_list.append({
                                    'title': title,
                                    'save_title': replace_not_sup_file_name(title),
                                    'id': id,
                                    'userId': userId,
                                    'userName': userName,
                                    'tags': tags,
                                    'url': url
                                })
                                print("id:", id, " dow OK !")
                                img_error_url.append({
                                    'title': title,
                                    'save_title': replace_not_sup_file_name(title),
                                    'id': id,
                                    'userId': userId,
                                    'userName': userName,
                                    'tags': tags,
                                    'url': url
                                })
                time.sleep(4)
        if old_id != ids[1]:
            old_id = ids[1]
            p = p + 1
            get_pixiv_img()


if __name__ == '__main__':
    flag = False
    try:
        get_pixiv_img()
    except Exception as e:
        flag = True
        b = img_id[-1]
        for i in img_id:
            if i == b:
                img_id.remove(i)
        raise e
    finally:
        with open('./img_id.index', 'w+', encoding="UTF-8") as f:
            for id in img_id:
                f.write(f"{id}\n")
        with open('./img_list.index', 'w+' if flag else 'a+', encoding="UTF-8") as f:
            for data in img_list:
                f.write(f"{json.dumps(data, ensure_ascii=False)}\n")
        with open('./img_error_url.error', 'w+', encoding="UTF-8") as f:
            for data in img_error_url:
                f.write(f"{json.dumps(data, ensure_ascii=False)}\n")
        with open('./update.index', 'w+', encoding="UTF-8") as f:
                f.write(str(need_update_img_id))