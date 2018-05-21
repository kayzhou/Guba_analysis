from emotion_cla.emo_cls import classify

import os
import json
import jieba

in_dir = 'data/tweet'
out_dir = 'data/tweet_emo'

for i, in_name in enumerate(os.listdir(in_dir)):
    print(i)
    stock_name = in_name
    in_name = os.path.join(in_dir, in_name)
    for j, line in enumerate(open(in_name)):
        d = json.loads(line)
        d['content_pre_emo'] = classify(d['content']) 
        d['title_pre_emo'] = classify(d['title'])
        with open('{}/{}'.format(out_dir, stock_name), 'a') as f:
            f.write(json.dumps(d, ensure_ascii=False) + '\n')
