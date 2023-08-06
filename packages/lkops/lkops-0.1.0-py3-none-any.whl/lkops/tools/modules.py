# -*- encoding: utf-8 -*-
'''
@Time    :   2022-09-01 09:58:53
@Author  :   songhaoyang
@Version :   1.0
@Contact :   songhaoyanga@enn.cn
'''
import os
import time
import json
import functools
import numpy as np


def clock(func):
    """this is outer clock function"""

    @functools.wraps(func)  # --> 4
    def clocked(*args, **kwargs):  # -- 1
        """this is inner clocked function"""
        start_time = time.time()
        result = func(*args, **kwargs)  # --> 2
        time_cost = time.time() - start_time
        if time_cost > 0.0:
            print(func.__name__ + " -> {} ms".format(int(1000 * time_cost)))
        return result

    return clocked


class NpEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


def join_path(p1, p2, p3=None):
    if p3:
        return os.path.join(p1, p2, p3)
    else:
        return os.path.join(p1, p2)