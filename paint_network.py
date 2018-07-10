import json
from tqdm import tqdm


data = {
    'nodes': [],
    'links': []
}

have_nodes = set([])
all_nodes = set([]) 

count = 0
for line in tqdm(open('data/follow-2.txt')):
    count += 1
    if count >= 100:
        break
    d = json.loads(line.strip())
    uid = d['user_id']
    f_links = d['following_list']
    if len(f_links) > 0:
        node = {"id": uid, "group": int(len(f_links) / 10)}
        have_nodes.add(uid)
    
    all_nodes.add(uid)
    data['nodes'].append(node)

    for u in f_links:
        link = {"source": uid, "target": u, "value": 1}
        all_nodes.add(u)
        data['links'].append(link)

left = all_nodes - have_nodes

for u in left:
    node = {"id": u, "group": 0} 
    data['nodes'].append(node)


json.dump(data, open('network_sample.json', 'w'), indent=1)

