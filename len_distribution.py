#!/usr/bin/env python
# encoding: utf-8

# 格力电器 000651
import os
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

in_dir = '/home/kayzhou/Project/Guba_spider/guba/data'
in_name = '/home/kayzhou/Project/Guba_spider/guba/data/000651.txt'

_list_len = []
for i, in_name in enumerate(os.listdir(in_dir)):
    print(i)
    in_name = os.path.join(in_dir, in_name)
    for j, line in enumerate(open(in_name)):
        # print(line)
        try:
            _list_len.append(len(json.loads(line)['content']))
        except:
            # print('Q&A')
            pass

_len = pd.Series(_list_len)
_len.to_csv('content_len.txt', index=None)

