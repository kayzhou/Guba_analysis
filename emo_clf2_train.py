import json
import os
from collections import Counter

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC
from thulac import thulac
from tqdm import tqdm_notebook as tqdm

thu = thulac(seg_only=True)


def load_stopword():
    """
    加载停用词集合
    """
    return set(json.load(open('data/stopword-zh.json')))


def load_train_data(in_name):
    """
    加载训练数据
    """
    X = []
    y = []
    for line in open(in_name):
        label, vec = line.strip().split('\t')
        x = np.array([float(v) for v in vec.split(',')])
        y.append(label)
        X.append(x)
    return X, y


def train():
#     X, y = load_train_data('train_data_one_hot-20180710.txt')
    X, y = load_train_data('train_data_ACL-20180710.txt')
    
    # 划分数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=41)
    
    # 初始化分类器
#     clf = RandomForestClassifier(max_depth=10, random_state=1)
#     clf = BernoulliNB()
    clf = SVC(C=0.5) # SVM较为耗时

    # 执行训练
    clf.fit(X_train, y_train)

    # 模型评估
    print(cross_val_score(clf, X, y, cv=10).mean())

    y_pred = []
    for i in range(len(X_test)):
        y = clf.predict(X_test[i].reshape(1, -1))
        # print(y[0])
        y_pred.append(y[0])
    print(classification_report(y_test, y_pred))
    
train()
