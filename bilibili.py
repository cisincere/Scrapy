import json
import random
import time

import requests

from entity.replay import Replay

replie_oid_data = []
reply = open('655375868.reply', 'w+', encoding="UTF-8")
last_time = {
    '655375868': ''
}


def pares_replay(data):
    global last_time
    replies = data['replies']
    for replie in replies:
        # if replie['replies'] is not None:
        #     pares_replay(replie)
        replay = Replay()
        replay.analyze_json(replie)
        if last_time['655375868'] == '':
            last_time['655375868'] = replay.ctime
        date = replay.__str__().replace("\n", '').replace("        ", '').replace('    ', '') + '\n'
        reply.write(date)


def get_reply(aid, next=None):
    BILI_URL = f'https://api.bilibili.com/x/v2/reply/main?mode=2&oid={aid}&plat=1&seek_rpid=&type=1'
    if next is not None:
        BILI_URL = f'https://api.bilibili.com/x/v2/reply/main?mode=2&oid={aid}&plat=1&seek_rpid=&type=1&next={next}'
    replay_text = requests.get(BILI_URL).text
    replay_json = json.loads(replay_text)
    if replay_json['code'] == 0:
        replay_data = replay_json['data']
        pares_replay(replay_data)
    return (replay_json['data']['cursor']['prev'], replay_json['data']['cursor']['next'])


# 1682657829
if __name__ == '__main__':
    prev, next = get_reply(655375868)
    for i in range(prev, 0, -1):
        time.sleep(random.randint(2, 6))
        get_reply(655375868, i)
    with open('update.index', 'w+', encoding="UTF-8") as f:
        f.write(json.dumps(last_time))
