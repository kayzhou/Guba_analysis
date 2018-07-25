## 遍历数据抽取关系
# 先只考虑tweet的用户
# 另外新闻、公告、研报和其他的数据不管

import json
import os
from collections import defaultdict

# 2 large dicts
USER_STOCK = {}
STOCK_USER = {}


def get_relation(in_name):
    for line in open(in_name):
        d = json.loads(line.strip())
        uid = d['uid']
        stock = d['stock_id']

        if uid not in USER_STOCK:
            USER_STOCK[uid] = defaultdict(int)
        USER_STOCK[uid][stock] += 1
        
        if stock not in STOCK_USER:
           STOCK_USER[stock] = defaultdict(int)
        STOCK_USER[stock][uid] += 1


if __name__ == '__main__':
    in_dir = '/home/kayzhouProject/Guba_spider/data/tweet'
    for in_name in os.listdir(in_dir):
        if in_name.endswith('.txt'):
            continue
        in_name = os.path.join(in_dir, in_name)
        get_relation(in_name)
        break

    with open('data/relation_user_stock.txt', 'w') as f:
        for uid in USER_STOCK:
            f.write(json.dumps(USER_STOCK[uid]) + '\n')

    with open('data/relation_stock_user.txt', 'w') as f:
        for stock in STOCK_USER:
            f.write(json.dumps(STOCK_USER[stock]) + '\n')



