import json
import os
import re
import numpy as np

import jieba
import linecache

from emotion_cla.emo_cls import classify
from emotion_cla.separate import separate

in_dir = 'data/tweet'
out_dir = 'data/tweet_emo'


def random_ids(in_name, lens):
    '''
    随机选择文本的行
    '''
    ids = set()
    _max = len(open(in_name).readlines())  
    for _ in range(lens):
        num = int(_max * np.random.random())
        if num in ids:
            continue
        line = linecache.getline(in_name, num)
        # _id = line.strip().split(',')[0]
        ids.add(num)
    return ids


def pre_label():
    '''
    打预标签
    '''
    for i, in_name in enumerate(os.listdir(in_dir)):
        print(i)
        stock_name = in_name
        in_name = os.path.join(in_dir, in_name)
        for j, line in enumerate(open(in_name)):
            d = json.loads(line)
            d['content_pre_emo'] = classify(separate(d['content']))
            d['title_pre_emo'] = classify(separate(d['title']))
            with open('{}/{}'.format(out_dir, stock_name), 'a') as f:
                f.write(json.dumps(d, ensure_ascii=False) + '\n')


def get_train_data(in_name):

    for line in open(in_name):
        d = json.loads(line.strip())
        content = d['content']
        title = d['title']
        t_emo = d['title_pre_emo']
        c_emo = d['content_pre_emo']
        
        # 标题和内容中要有一个有表情符
        # if not (re.search('\\[\\S+\\]', title) or re.search('\\[\\S+\\]', content)):
        if not re.search('\\[\\S+\\]', content):
            print('不满足要求 ...')
            continue

        # 内容长度5到200
        if 5 < len(content) < 200:
            with open('data/content/{}.txt'.format(c_emo), 'a') as f:
                f.write(str(c_emo) + '\t' + content + '\n')

        # with open('data/title/{}.txt'.format(t_emo), 'a') as f:
        #     f.write(str(t_emo) + '\t' + title + '\n')
        

if __name__ == '__main__':
    for line in open('data/random_ids.txt'):
        in_name = 'data/tweet_emo/' + line.strip() + '.txt'
        get_train_data(in_name)
    # random_ids('data/_id.txt', 100)
    # get_train_data('data/002446.txt')
