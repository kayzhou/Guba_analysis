# 过滤信息，分为xinwen,yanbao,tweet，还有不可识别
# 还有过滤掉无用的信息
import os
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


in_dir = '/home/kayzhou/Project/Guba_spider/guba/data'
in_name = '/home/kayzhou/Project/Guba_spider/guba/data/000651.txt'

def get_type(content):
    if content.startswith('来源：'):
        return 'xinwen'
    elif content.startswith('研报日期：'):
        return 'yanbao'
    elif content.startswith('公告日期：'):
        return 'gonggao'
    else:
        return 'tweet'


def delete_log(t):
    del t['download_timeout']
    del t['depth']
    del t['download_slot']
    del t['download_latency']
    return t


for i, in_name in enumerate(os.listdir(in_dir)):
    print(i, in_name)
    stock_name = in_name
    in_name = os.path.join(in_dir, in_name)
    for j, line in enumerate(open(in_name)):
        # print(line)
        d = delete_log(json.loads(line))
        if 'content' in d:
            _type = get_type(d['content'])
        else:
            _type = 'others'
        with open('data/{}/{}'.format(_type, stock_name), 'a') as f:
            f.write(json.dumps(d, ensure_ascii=False) + '\n')
