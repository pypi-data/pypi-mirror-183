# -*- encoding: utf-8 -*-
'''
@Time    :   2022-10-18 14:30:10
@Author  :   songhaoyang
@Version :   1.0
@Contact :   songhaoyanga@enn.cn
'''

import time
from concurrent.futures import ThreadPoolExecutor


def task(*args, **kwargs):
    print("start thread task.")
    print(args, "\n", kwargs)
    time.sleep(1)
    print("*****************")
    print("finish task after 1s.")


if __name__ == "__main__":
    # 创建线程池
    thread_pool = ThreadPoolExecutor(max_workers=10)
    thread_pool.submit(task, "a", "b", c="cc", d="dd")
    print("finsh main process.")
