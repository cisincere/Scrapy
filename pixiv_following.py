import json
import os
import time

import requests

#

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ga;q=0.6,zh-TW;q=0.5",
    "cache-control": "no-cache",
    "Referer": "https://www.pixiv.net/",
    "X-User-Id": "32081625",
    "Sec-Ch-Ua": """\"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114\"""",
    "cookie": """first_visit_datetime_pc=2023-04-19+12%3A41%3A05; p_ab_id=6; p_ab_id_2=7; p_ab_d_id=256691513; yuid_b=NQGZJDM; __utmz=235335808.1681875668.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _fbp=fb.1.1681875668722.1254211920; c_type=28; privacy_policy_notification=0; a_type=0; b_type=2; __utmc=235335808; PHPSESSID=32081625_oDf3J1tYppgDzLksIbuhW3QbYJj6z5DP; device_token=6fe5af4106efc7860f6fb03079221931; _ga_MZ1NL4PHH0=GS1.1.1687664407.2.1.1687664464.0.0.0; _im_vid=01H3RA8M2SEAASFS5K0J366T7Y; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=female=1^6=user_id=32081625=1^9=p_ab_id=6=1^10=p_ab_id_2=7=1^11=lang=zh=1; _gcl_au=1.1.89918381.1688451800; _im_uid.3929=i.JoPPTYAVTxCfj7OIt78jCw; privacy_policy_agreement=6; tag_view_ranking=Lt-oEicbBr~RTJMXD26Ak~LJo91uBPz4~jH0uD88V6F~fg8EOt4owo~qtVr8SCFs5~uW5495Nhg-~eVxus64GZU~Ie2c51_4Sp~65aiw_5Y72~tgP8r-gOe_~b_rY80S-DW~nQRrj5c6w_~zyKU3Q5L4C~pzzjRSV6ZO~5oPIfUbtd6~yjXuOIRb29~6rYZ-6JKHq~kGYw4gQ11Z~K8esoIs2eW~EUwzYuPRbU~LtW-gO6CmS~CMH7y9clRf~DpO7Lofslr~RybylJRnhJ~d2oWv_4U1L~_EOd7bsGyl~KOnmT1ndWG~azESOjmQSV~m8jdSenntp~1LN8nwTqf_~YRDwjaiLZn~28gdfFXlY7~kMjNs0GHNN~NBK37t_oSE~B9VsvJr9Z4~pYlUxeIoeg~L58xyNakWW~f4V1aCLsyM~I5npEODuUW~HBlflqJjBZ~q303ip6Ui5~-StjcwdYwv~QaiOjmwQnI~eK9vnMvjjT~HLWLeyYOUF~Sjwi7bh6-s~nktHt4eKXE~BtXd1-LPRH~Mt2C8GjPNp~b1s-xqez0Y~y3NlVImyly~SoxapNkN85~PTyxATIsK0~jPsOGzt9Dh~9bexjBsjKX~6RcLf9BQ-w~Xyw8zvsyR4~cxG7coNmIs~ylO3Y-Ere0~ko30YJxw7F~RolC8IrBVO~z0yXlSLXfe~8JWNewp8W3~xvvNXPv-9y~JMZLFJTqqo~OVcez6CxIO~a-IhwNF_3B~RJgdaZTe9a~WY10GFG4q3~Xs3nxH7Ckz~GFExx0uFgX~CrFcrMFJzz~tZoj8l9PLN~HffPWSkEm-~kqu7T68WD3~tIqkVZurKP~1yIPTg75Rl~j3leh4reoN~Bd2L9ZBE8q~Bs22qPIxHA~TUVB-oxjcR~Ged1jLxcdL~KYZac79H5v~KwjO9A0Kl6~cryvQ5p2Tx~RBqBcZh7ix~ay54Q_G6oX~Ed_W9RQRe_~KexWqtgzW1~KN7uxuR89w~zXUuIJGfCn~XDEWeW9f9i~_pwIgrV8TB~3SAZKPd9Ah~BQFWWhxtER~-qP3pM5H97~PGh9Qwfchx~mqf4KYn6Dx~rGIDVSTFJU; cto_bundle=FTVCe19ERUJteExadzB2Rm5CMkRiUmdXWGRiUiUyRjZCTEdCZU5nV0RtMWVvQlgwdkFqQlVzVEN1aUduRFlhcVFkdUNnRHZObzlUWXNWeiUyQnRyZEVCOW1tdlJOakhlQ2NRJTJCSVhVYUVLMHlMYkszbU82dU5zZEolMkJIYXhEenR5T1FRNndoMFg2eGphWlJjbk43RmcxdlFaTFFxZ2pyZyUzRCUzRA; _ga=GA1.1.114644716.1681875668; __utma=235335808.114644716.1681875668.1689232799.1689643120.31; __utmt=1; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; _ga_75BBYNYN9J=GS1.1.1689643120.36.1.1689643153.0.0.0; __cf_bm=q91Iwdh3H1UgpEsW4EeYxCofJ.b2pWubB.3k8Yf06P0-1689643154-0-AdzqJMmXoXAUkcQfXmiFGpSuqH7sNq2nBQCq+Catlq2qyV3s2fdqGCIBpvfmP1QnCLB/y0oKOb4iHiW7Nklpw4IFIMm+NcAGu6pie2GWaOr9dZw49kR+bj0nwjcB77nhOg==; __utmb=235335808.2.10.1689643120"""
}
not_sup_file_name = ['/', '\\', '<', '>', ':', '"', '|', '*', '?']


def replace_not_sup_file_name(title: str) -> str:
    for item in not_sup_file_name:
        title = title.replace(item, '~')
    return title


def load_following() -> list:
    result = []
    with open('./following.index', 'r', encoding="UTF-8") as f:
        for line in f.readlines():
            result.append(line.strip())
    return result


def load_follow_img_id_list() -> list:
    result = []
    with open('./follow_img_id_list.list', 'r', encoding="UTF-8") as f:
        for line in f.readlines():
            result.append(line.strip())
    return result


def load_follow_user_follow_list() -> list:
    result = []
    with open('./follow_user_follow.index', 'r', encoding="UTF-8") as f:
        for line in f.readlines():
            result.append(line.strip())
    return result


def load_img_id() -> list:
    result = []
    with open('./img_id.index', 'r', encoding="UTF-8") as f:
        for line in f.readlines():
            result.append(line.strip())
    return result


following_list = load_following()
follow_img_id_list = load_follow_img_id_list()
follow_user_follow_list = load_follow_user_follow_list()
no_save_tag = ['男孩子', 'スーツ男子', '男子', '男の子', 'boy', '남자애']
img_ids = load_img_id()


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


def check_tags(img_info_map: dict) -> bool:
    tags = img_info_map.get('tags', {}).get('tags', [])
    for tag in tags:
        org_tag = tag.get('tag', '')
        trans_tag = tag.get('translation', {}).get('en', '')
        if org_tag in no_save_tag or trans_tag in no_save_tag:
            return False
    return True


def fetch_img_info(img_id: str):
    global headers
    uri = f'https://www.pixiv.net/ajax/illust/{img_id}?lang=zh&version=3458ffd6ed8e7339f4354c3577f0d991c3bd9e3f'
    result = requests.get(uri, headers=headers)
    img_info_json = json.loads(result.text)
    return img_info_json.get('body', {})


def fetch_img_uri(img_id: str):
    global headers
    global follow_img_id_list
    user_img_id = img_id.split(',')
    uri = f'https://www.pixiv.net/ajax/illust/{user_img_id[-1]}/pages?lang=zh&version=b9b078e20f148df8e35775f2381957c1466c9ab3'
    img_info_map = fetch_img_info(user_img_id[-1])
    title = replace_not_sup_file_name(img_info_map.get('title', 'NO_IMG_NAME'))
    if check_tags(img_info_map):
        result = requests.get(uri, headers=headers)
        all_img_json = json.loads(result.text)
        if not all_img_json.get('error', True):
            body = all_img_json.get('body', [])
            for index, b in enumerate(body):
                urls = b.get('urls', {})
                img_uri = urls.get('original', '')
                regular = urls.get('regular', '')
                if len(img_uri) < 1:
                    img_uri = regular
                yield (user_img_id[0], user_img_id[-1], img_uri, f'{title}_{index}')


def follow_all_img_id(user_id):
    global headers
    global follow_img_id_list
    uri = f'https://www.pixiv.net/ajax/user/{user_id}/profile/all?lang=zh&version=b9b078e20f148df8e35775f2381957c1466c9ab3'
    result = requests.get(uri, headers=headers)
    all_img_json = json.loads(result.text)
    if not all_img_json.get('error', True):
        body = all_img_json.get('body', {})
        illusts = body.get('illusts', {})
        try:
            img_ids = illusts.keys()
            for ii in img_ids:
                if f'{user_id},{ii}' not in follow_img_id_list:
                    follow_img_id_list.append(f'{user_id},{ii}')
        except Exception as e:
            print(illusts)
            raise e


def fetch_follow(follow_list, user_id, offset=0, limit=24):
    global headers
    global following_list
    BASE_URL = f'https://www.pixiv.net/ajax/user/{user_id}/following?offset={offset}&limit={limit}&rest=show&tag=&acceptingRequests=0&lang=zh&version=b9b078e20f148df8e35775f2381957c1466c9ab3'
    result = requests.get(BASE_URL, headers=headers)
    following_json = json.loads(result.text)
    if not following_json.get('error', True):
        body = following_json.get('body', {})
        total = body.get('total', 0)
        users = body.get('users', [])
        for user in users:
            tmp_user_id = user.get('userId', 'Rinko')
            if tmp_user_id not in follow_list and tmp_user_id not in following_list:
                follow_list.append(tmp_user_id)
        if offset + limit < total:
            time.sleep(5)
            fetch_follow(follow_list, user_id, offset + 24, 24)


def fetch_following(offset=0, limit=24):
    global headers
    global following_list
    BASE_URL = f'https://www.pixiv.net/ajax/user/32081625/following?offset={offset}&limit={limit}&rest=show&tag=&acceptingRequests=0&lang=zh&version=b9b078e20f148df8e35775f2381957c1466c9ab3'
    result = requests.get(BASE_URL, headers=headers)
    following_json = json.loads(result.text)
    if not following_json.get('error', True):
        body = following_json.get('body', {})
        total = body.get('total', 0)
        users = body.get('users', [])
        for user in users:
            user_id = user.get('userId', 'Rinko')
            if user_id not in following_list:
                following_list.append(user_id)
        if offset + limit < total:
            time.sleep(2)
            fetch_following(offset + 24, 24)


if __name__ == '__main__':
    import sys

    arg = sys.argv
    tmp_list = []
    try:
        if '-f' in arg:
            fetch_following()
        if '-fuf' in arg:
            for id in following_list:
                print(id)
                if id not in follow_user_follow_list:
                    fetch_follow(tmp_list, id)
                    follow_user_follow_list.append(id)
                    time.sleep(5)
        if '-fi' in arg:
            for f in following_list:
                follow_all_img_id(f)
                time.sleep(3)
        if '-m' in arg:
            for f in follow_img_id_list:
                user_img_id = f.split(',')
                if user_img_id[-1] not in img_ids:
                    # https://www.pixiv.net/ajax/user/3388329/illusts?ids%5B%5D=101808062&lang=zh&version=b9b078e20f148df8e35775f2381957c1466c9ab3
                    for user_id, img_id, img_uri, title in fetch_img_uri(f):
                        print(user_id, img_id, img_uri, title)
                        if img_uri is not None:
                            dow_img(img_uri, user_id, img_id, title, img_uri.split(".")[-1])
                    img_ids.append(user_img_id[-1])
                    time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        following_list.extend(tmp_list)
        with open('./following.index', 'w+', encoding="UTF-8") as f:
            for id in following_list:
                f.write(f"{id}\n")
        with open('./follow_img_id_list.list', 'w+', encoding="UTF-8") as f:
            for id in follow_img_id_list:
                f.write(f"{id}\n")
        with open('./follow_user_follow.index', 'w+', encoding="UTF-8") as f:
            for id in follow_user_follow_list:
                f.write(f"{id}\n")
        with open('./img_id.index', 'w+', encoding="UTF-8") as f:
            for id in img_ids:
                f.write(f"{id}\n")
