# https://www.pixiv.net/ajax/follow_latest/illust?p=2&mode=all&lang=zh
# https://www.pixiv.net/ajax/illust/107600377


import json
import os
import time

import requests

BASE_URL = 'https://www.pixiv.net/ajax/illust/'


def load_img_id() -> []:
    result = []
    with open('./img_id.index', 'r', encoding="UTF-8") as f:
        for line in f.readlines():
            result.append(line.strip())
    return result


img_id = load_img_id()


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


def get_pixiv_img():
    global img_list
    global img_id
    global old_id
    global p
    global log
    global img_error_url
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ga;q=0.6,zh-TW;q=0.5",
        "cache-control": "no-cache",
        "cookie": """first_visit_datetime_pc=2023-04-19+12%3A41%3A05; p_ab_id=6; p_ab_id_2=7; p_ab_d_id=256691513; yuid_b=NQGZJDM; __utmz=235335808.1681875668.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _fbp=fb.1.1681875668722.1254211920; PHPSESSID=32081625_CI9765VMgwYHD0BB0cGBnTWHBTCZUqob; device_token=19bb6837105f8ceff67d3a4b5a57e291; privacy_policy_agreement=5; c_type=28; privacy_policy_notification=0; a_type=0; b_type=2; _ga_MZ1NL4PHH0=GS1.1.1681875670.1.1.1681875716.0.0.0; __utmv=235335808.|2=login%20ever=no=1^3=plan=normal=1^5=gender=female=1^6=user_id=32081625=1^9=p_ab_id=6=1^10=p_ab_id_2=7=1^11=lang=zh=1; _im_vid=01GYBSNQ4Q66HJH6DM4E0DM9FW; __utma=235335808.114644716.1681875668.1681969981.1683688758.4; __utmc=235335808; __cf_bm=kZE0waXVhpfL0JSIPvvJ6_06NthjTkMhs8OowyQt6aE-1683688759-0-AXnsKAKnaYLf+J4LHIB0cbzYno/Cp+ggmK/nf3kkWkwJdAhNaa8CxX0jHMtEcFf1gAR3niN5Ar00pWerZ4BSeEl57L34pDU1o7H8ptqz/X7CIBLAt16LmKXD8DUmVB+VroyqpqsUE1i6rFW4yNupjtomJRNqc5Xmj0EHoAT1Rgx9; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; _ga=GA1.2.114644716.1681875668; _gid=GA1.2.1035871944.1683688843; _ga_75BBYNYN9J=GS1.1.1683688759.4.1.1683689062.0.0.0; __utmb=235335808.4.10.1683688758; tag_view_ranking=65aiw_5Y72~kGYw4gQ11Z~RTJMXD26Ak~y6s3rcoyX3~b_CyxtxIQi~FaGmAtImEK~DtYwfCYeRB~kP7msdIeEU~HBYFbIUAS8~LJo91uBPz4~Lt-oEicbBr~Bs22qPIxHA~OQy7Z2HQT0~b-s2K-esBC~Sn_ZA5Y16t~xb-vAio_xa~koDwab9L0J~HY55MqmzzQ~b1s-xqez0Y~B_mnKj167d~pMiIF_RNwT~4ZEPYJhfGu~Yzt815Kiuz~nqrApWa41s~qQ77lqOSk3~7kHMYSX6tr~Bd2L9ZBE8q~KN7uxuR89w~gVfGX_rH_Y~UNmUR27_Et~ZRGAWQ4_eJ; cto_bundle=fLImh19ERUJteExadzB2Rm5CMkRiUmdXWGRiRFFrbmxNcUJPUmQ3cnRnOEslMkY0U1ZWSlBOQ0p0RW03cjlRMjQlMkZyNlRlRG5Rc3hrRzJRaGw4WndPOVNLSzFYdzFhdFE4R05pNms0MVFnMnJLdmhHMW9MUSUyQnc2ZWNMU3N0Sm5CSkM3Nm9ocEZtaFN5TlFpS3BLZGJXTnM2Rm1qVkElM0QlM0Q"""
    }
    result = requests.get(f'https://www.pixiv.net/ajax/follow_latest/illust?p={p}&mode=all&lang=zh', headers=headers)
    log.write(f'https://www.pixiv.net/ajax/follow_latest/illust?p={p}&mode=all&lang=zh\n')
    pixiv_json = json.loads(result.text)
    log.write(f"{json.dumps(pixiv_json, ensure_ascii=False)}\n")
    if not pixiv_json.get('error', True):
        body = pixiv_json.get('body', {})
        ids = pixiv_json.get('body', {}).get('page', {}).get('ids', [''])
        tagTranslation = body.get('tagTranslation')
        thumbnails = body.get('thumbnails', {})
        illust_list = thumbnails.get('illust', [])
        for illust in illust_list:
            title = illust.get('title', 'Rinko')
            id = illust.get('id', '')
            userId = illust.get('userId', 'Rinko')
            userName = illust.get('userName', 'Rinko')
            tags = ",".join(parse_tag(illust.get('tags', []), tagTranslation))
            if len(id) > 0 and id not in img_id:
                illust_result = requests.get(BASE_URL + id + '/pages', headers=headers)
                pixiv_illust_json = json.loads(illust_result.text)
                if not pixiv_illust_json.get('error', True):
                    illust_body = pixiv_illust_json.get('body', [])
                    for index, ib in enumerate(illust_body):
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
                            if len(illust_body) > 2:
                                time.sleep(1)
                        except Exception as e:
                            img_error_url.append({
                                'title': title,
                                'save_title': replace_not_sup_file_name(title),
                                'id': id,
                                'userId': userId,
                                'userName': userName,
                                'tags': tags,
                                'url': url
                            })
            time.sleep(2)
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
