# -*- encoding: utf-8 -*-
'''
@Time    :   2022-11-09 17:47:50
@Author  :   songhaoyang
@Version :   1.0
@Contact :   songhaoyanga@enn.cn
'''

import time
import threading
from gevent import pywsgi
from flask import Flask
from flask_apscheduler import APScheduler
from flask_apscheduler.auth import HTTPBasicAuth


# 定时任务模块
class Config(object):
    # 设置时区，时区不一致会导致定时任务的时间错误
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    # 一定要开启API功能，这样才可以用api的方式去查看和修改定时任务
    SCHEDULER_API_ENABLED = True
    # api前缀（默认是/scheduler）
    SCHEDULER_API_PREFIX = '/scheduler'
    # auth验证。默认是关闭的，
    SCHEDULER_AUTH = HTTPBasicAuth()


scheduler = APScheduler()
application = Flask(__name__)
application.config.from_object(Config)

# 指定间隔任务
@scheduler.task('interval', id='do_job_1', seconds=3, misfire_grace_time=900)
def _job1():
    thread_id = threading.currentThread().ident
    time_stamp = time.time()
    time_array = time.localtime(time_stamp)
    other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    print(f"线程:{thread_id}， time:{other_style_time}")

# 定时触发任务
@scheduler.task(trigger='cron', id='pre_load_data', day='*', hour='23', minute='59', second='59')
def _timing_task_reload_data_diet():
    try:
        thread_id = threading.currentThread().ident
        print(f"thread-{thread_id}-start the auto task pre_load_data.")
        print(f"thread-{thread_id}-load data success")
    except Exception as error:
        msg = repr(error)
        print(f"自动加载数据error, {msg}")


application.config.from_object(Config)
scheduler.init_app(application)
scheduler.start()

if __name__ == "__main__":
    ip = "0.0.0.0"
    port = 65534
    server = pywsgi.WSGIServer((ip, port), application)
    print(f"start at {ip}:{port}")
    server.serve_forever()
