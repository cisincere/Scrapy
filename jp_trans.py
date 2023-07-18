BASE_PATH = 'C:\\work\\Web\\qwerty-learner\\public\\dicts'
BASE_URL = 'https://www2.deepl.com/jsonrpc?method=LMT_handle_jobs'
headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ga;q=0.6,zh-TW;q=0.5",
        "cache-control": "no-cache",
        "cookie": """first_visit_datetime_pc=2023-04-19+12%3A41%3A05; p_ab_id=6; p_ab_id_2=7; p_ab_d_id=256691513; yuid_b=NQGZJDM; __utmz=235335808.1681875668.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _fbp=fb.1.1681875668722.1254211920; PHPSESSID=32081625_CI9765VMgwYHD0BB0cGBnTWHBTCZUqob; device_token=19bb6837105f8ceff67d3a4b5a57e291; privacy_policy_agreement=5; c_type=28; privacy_policy_notification=0; a_type=0; b_type=2; _ga_MZ1NL4PHH0=GS1.1.1681875670.1.1.1681875716.0.0.0; __utmv=235335808.|2=login%20ever=no=1^3=plan=normal=1^5=gender=female=1^6=user_id=32081625=1^9=p_ab_id=6=1^10=p_ab_id_2=7=1^11=lang=zh=1; _im_vid=01GYBSNQ4Q66HJH6DM4E0DM9FW; __utma=235335808.114644716.1681875668.1681969981.1683688758.4; __utmc=235335808; __cf_bm=kZE0waXVhpfL0JSIPvvJ6_06NthjTkMhs8OowyQt6aE-1683688759-0-AXnsKAKnaYLf+J4LHIB0cbzYno/Cp+ggmK/nf3kkWkwJdAhNaa8CxX0jHMtEcFf1gAR3niN5Ar00pWerZ4BSeEl57L34pDU1o7H8ptqz/X7CIBLAt16LmKXD8DUmVB+VroyqpqsUE1i6rFW4yNupjtomJRNqc5Xmj0EHoAT1Rgx9; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; _ga=GA1.2.114644716.1681875668; _gid=GA1.2.1035871944.1683688843; _ga_75BBYNYN9J=GS1.1.1683688759.4.1.1683689062.0.0.0; __utmb=235335808.4.10.1683688758; tag_view_ranking=65aiw_5Y72~kGYw4gQ11Z~RTJMXD26Ak~y6s3rcoyX3~b_CyxtxIQi~FaGmAtImEK~DtYwfCYeRB~kP7msdIeEU~HBYFbIUAS8~LJo91uBPz4~Lt-oEicbBr~Bs22qPIxHA~OQy7Z2HQT0~b-s2K-esBC~Sn_ZA5Y16t~xb-vAio_xa~koDwab9L0J~HY55MqmzzQ~b1s-xqez0Y~B_mnKj167d~pMiIF_RNwT~4ZEPYJhfGu~Yzt815Kiuz~nqrApWa41s~qQ77lqOSk3~7kHMYSX6tr~Bd2L9ZBE8q~KN7uxuR89w~gVfGX_rH_Y~UNmUR27_Et~ZRGAWQ4_eJ; cto_bundle=fLImh19ERUJteExadzB2Rm5CMkRiUmdXWGRiRFFrbmxNcUJPUmQ3cnRnOEslMkY0U1ZWSlBOQ0p0RW03cjlRMjQlMkZyNlRlRG5Rc3hrRzJRaGw4WndPOVNLSzFYdzFhdFE4R05pNms0MVFnMnJLdmhHMW9MUSUyQnc2ZWNMU3N0Sm5CSkM3Nm9ocEZtaFN5TlFpS3BLZGJXTnM2Rm1qVkElM0QlM0Q"""
    }
param = {
  "jsonrpc": "2.0",
  "method": "LMT_handle_jobs",
  "params": {
    "jobs": [
      {
        "kind": "default",
        "sentences": [
          {
            "text": "hello", # 修改
            "id": 0,
            "prefix": ""
          }
        ],
        "raw_en_context_before": [],
        "raw_en_context_after": [],
        "preferred_num_beams": 5
      }
    ],
    "lang": {
      "preference": {
        "weight": {
          "DE": 0.19568,
          "EN": 5.02862,
          "ES": 0.23486,
          "FR": 0.15568,
          "IT": 0.10938,
          "JA": 0.52504,
          "NL": 0.14285,
          "PL": 0.06732,
          "PT": 0.06951,
          "RU": 0.07069,
          "ZH": 8.11412,
          "CS": 0.05029,
          "DA": 0.22628,
          "ET": 0.04976,
          "FI": 0.06028,
          "HU": 0.04898,
          "LT": 0.04528,
          "LV": 0.03857,
          "RO": 0.04659,
          "SK": 0.04776,
          "SL": 0.05078,
          "SV": 0.14723,
          "TR": 0.06511,
          "ID": 0.06079,
          "KO": 0.08747,
          "NB": 0.2089,
          "BG": 0.04747,
          "EL": 0.04491,
          "UK": 0.05447
        },
        "default": "default"
      },
      "source_lang_user_selected": "EN",
      "target_lang": "ZH"
    },
    "priority": 1,
    "commonJobParams": {
      "mode": "translate",
      "browserType": 1
    },
    "timestamp": 1685509796910
  },
  "id": 56850015
}
import os
import json
import requests
import time
import shutil
def is_chinese(string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
 
    return False


def get_trans(text) -> list:
    param['params']['jobs'][0]['sentences'][0]['text'] = text
    param['params']['timestamp'] = int(time.time())
    res = requests.post(BASE_URL, headers=headers,json=param)
    result = json.loads(res.text)
    print(result)
    translations = result.get('result', {}).get('translations', [])
    trans = []
    for translation in translations:
        beams = translation.get('beams', [])
        for beam in beams:
            r = beam.get('sentences', [{}])[0].get('text', '')
            if len(r) < 1:
                r = text
            trans.append(r.replace("。", ''))
    return trans


for root, dirs, files in os.walk(BASE_PATH):
    for file in files:
        if 'Jap' in file and '.bak' not in file:
            jap_data = []
            flag = True
            with open(f'{BASE_PATH}\\{file}', 'r', encoding="UTF-8") as f:
                data = f.read()
                jap_labn_data = json.loads(data)
                for jap_labn in jap_labn_data:
                    chinese_trans = []
                    trans = jap_labn.get('trans', [])
                    if not is_chinese("".join(trans)):
                        for tran in trans:
                            chinese_trans.extend(get_trans(tran))
                            time.sleep(15)
                        jap_labn['trans'] = chinese_trans
                        jap_labn['old_trans'] = trans
                        jap_data.append(jap_labn)
                    else:
                        flag = False
                        break
            if flag:
                shutil.copy2(f'{BASE_PATH}\\{file}', f'{BASE_PATH}\\{file}.bak')
                with open(f'{BASE_PATH}\\{file}', 'w', encoding="UTF-8") as f:
                    f.write(json.dumps(jap_data, ensure_ascii=False))