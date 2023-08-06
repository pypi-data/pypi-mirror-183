# -*- encoding: utf-8 -*-
'''
@Time    :   2022-10-18 14:17:22
@Author  :   songhaoyang
@Version :   1.0
@Contact :   songhaoyanga@enn.cn
'''

import redis
import json

pool = redis.ConnectionPool(
    host="10.4.164.240",
    port=6379,
    db=0,
    password=None,
    decode_responses=True
)
conn = redis.StrictRedis(connection_pool=pool,)
print(json.loads(conn.get("0")))
