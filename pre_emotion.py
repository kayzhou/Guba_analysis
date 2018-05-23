import json
import os
import re

import jieba

from emotion_cla.emo_cls import classify
from emotion_cla.separate import separate

in_dir = 'data/tweet'
out_dir = 'data/tweet_emo'


def pre_label():
    '''
    打标签
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
        if not re.search('\\[\\S+\\]', title):
            print('不满足要求')
            continue
        if 0 < len(content) < 200:
            with open('data/content/{}.txt'.format(c_emo), 'a') as f:
                f.write(str(c_emo) + '\t' + content + '\n') 
        with open('data/title/{}.txt'.format(t_emo), 'a') as f:
            f.write(str(t_emo) + '\t' + title + '\n')
        

if __name__ == '__main__':
    get_train_data('data/002446.txt')
