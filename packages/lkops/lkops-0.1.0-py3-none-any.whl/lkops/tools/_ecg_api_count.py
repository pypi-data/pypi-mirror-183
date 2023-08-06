# -*- encoding: utf-8 -*-
'''
@Time    :   2022-09-13 16:38:52
@Author  :   songhaoyang
@Version :   1.0
@Contact :   songhaoyanga@enn.cn
'''
import os
import sys
import time
import json
import pickle
sys.path.append(os.path.dirname("."))

from conn._mysql import MysqlConnector
from collections import defaultdict




conn = MysqlConnector(user="ai", passwd="ai12345678",
                      ip="10.39.32.45", port=32125, db_name="four-diagnosis-copy")
data_ecg = conn.query(
    "select update_time from palpation_diagnosis where type=31")


def time_trans(timestamp):
    y = str(timestamp.year)
    m = str(timestamp.month)
    if len(m) == 1:
        m = f"0{m}"
    d = str(timestamp.day)
    if len(d) == 1:
        d = f"0{d}"
    return int(y+m)


count_ecg = defaultdict()
for i in data_ecg:
    ts = time_trans(i['update_time'])
    if count_ecg.get(ts):
        count_ecg[ts] += 1
    else:
        count_ecg[ts] = 1
data_ppg = conn.query(
    "select update_time from palpation_diagnosis where type=32")
count_ppg = defaultdict()
for i in data_ppg:
    ts = time_trans(i['update_time'])
    if count_ppg.get(ts):
        count_ppg[ts] += 1
    else:
        count_ppg[ts] = 1

# 1 已获得数据  0 未获得数据 11 食材状态
smelling_diagnosis = conn.query(
    "select create_time, status from smelling_diagnosis")
count_smelling = defaultdict()
for i in smelling_diagnosis:
    ts = time_trans(i['create_time'])
    if count_smelling.get(ts):
        count_smelling[ts] += 1
    else:
        count_smelling[ts] = 1

res = {"ecg": count_ecg, "ppg": count_ppg, "smell": count_smelling}
json.dump(res, open("ecg_api_count.json", "w", encoding='utf-8'),
          indent=4, ensure_ascii=False)
