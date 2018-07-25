## 遍历数据抽取关系
# 先只考虑tweet的用户
# 另外新闻、公告、研报和其他的数据不管

from tqdm import tqdm
import json
import os
from collections import defaultdict

# 2 large dicts
USER_STOCK = {}
STOCK_USER = {}


def get_relation(in_name):
    global USER_STOCK
    global STOCK_USER
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
    in_dir = '/home/kayzhou/Project/Guba_spider/data/tweet/'
    for in_name in tqdm(os.listdir(in_dir)):
        in_name = os.path.join(in_dir, in_name)
        if not in_name.endswith('.txt'):
            continue
        get_relation(in_name)

    with open('data/relation_user_stock.txt', 'w') as f:
        for uid in USER_STOCK:
            f.write(uid + ' @@ ' + json.dumps(USER_STOCK[uid]) + '\n')

    with open('data/relation_stock_user.txt', 'w') as f:
        for stock in STOCK_USER:
            f.write(stock + '@@' + json.dumps(STOCK_USER[stock]) + '\n')



