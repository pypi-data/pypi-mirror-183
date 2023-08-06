# -*- encoding: utf-8 -*-
'''
@Time    :   2022-11-14 11:43:48
@Author  :   songhaoyang
@Version :   1.0
@Contact :   songhaoyanga@enn.cn
'''
import os
import sys
import loguru
import socket

sys.path.append(os.path.dirname(sys.path[0]))
from tools.modules import join_path


"""
|   Level       | Severity value    |  Logger method       | 
|   TRACE       | 5                 |  logger.trace()      |
|   DEBUG       | 10                |  logger.debug()      |
|   INFO        | 20                |  logger.info()       |
|   SUCCESS     | 25                |  logger.success()    |
|   WARNING     | 30                |  logger.warning()    |
|   ERROR       | 40                |  logger.error()      |
|   CRITICAL    | 50                |  logger.critical()   |
"""


class Logging:
    """
    使用说明 修改appid
    from utils.Logger import Logging
    logger = Logging()
    logger.trace("asdf")
    """

    def __init__(self, kwargs) -> None:
        """
        修改配置appid 
        appid: 应用id
        console_level: 控制台日志级别 
        file_level: 保存文件日志级别
        online: 是否在线 默认true 日志存储到/data/logs/{appid}/{hostname}
                否 存储到./logs
        is_save: 是否添加存储logger的headle_id
        """
        appid = kwargs.get("appid", None)
        assert isinstance(appid, str), TypeError("illegal type for appid")

        console_level = kwargs.get("console_level", "DEBUG")
        file_level = kwargs.get("file_level", "INFO")
        is_save = kwargs.get("is_save", True)
        rebuild = kwargs.get("rebuild", False)

        _logger = loguru.logger

        if rebuild:
            _logger.remove()  # 删除原来的样式

            # 设置控制台打印不同颜色的log
            _logger.level('DEBUG', color='<blue>')
            _logger.level('INFO', color='<green>')
            _logger.level('WARNING', color='<yellow>')
            _logger.level('ERROR', color='<red>')
            _logger.level('CRITICAL', color='<magenta>')

            # 控制台输出
            # 如果devops日志平台检测存在格式错误
            _logger.add(
                sink=sys.stderr,
                format='<level>[{time:YYYY-MM-DD HH:mm:ss.SSS}] [{level}] [{process}] {module}:{name}:{line} {message}</level>',
                level=console_level,  # 设置log的level等级
                colorize=True,  # 开启颜色
                backtrace=True,
                diagnose=True)

        # devops要求日志保存在/data/logs/{appid}/{hostname}/{apppid}.log 系统自动采集
        hostname = socket.gethostname()
        log_dir = join_path("/data/logs", appid, hostname)
        try:
            os.makedirs(log_dir, exist_ok=True)
        except BaseException as error:
            print(repr(error))
            log_dir = "./logs"
            os.makedirs(log_dir, exist_ok=True)

        log_path = join_path(log_dir, f"{appid}.log")
        frat = "[{time:YYYY-MM-DD HH:mm:ss.SSS}] [{level}] [{process}] {module}:{name}:{line} {message}"

        # 文件输出
        if is_save:
            _logger.add(sink=log_path,
                        format=frat,
                        level=file_level,
                        encoding="utf-8",
                        rotation="50 MB",
                        retention="10 days",
                        compression="gz",
                        backtrace=True,
                        diagnose=True)
        self.logger = _logger


def get_logger(**kwargs):
    """
    @param
    """
    return Logging(kwargs).logger


if __name__ == "__main__":
    logger = get_logger(appid="test", rebuild=False)

    logger.trace("log level trace.")
    logger.debug("log level debug.")
    logger.info("log level info.")
    logger.success("log level success.")
    logger.warning("log level warning.")
    logger.error("log level error.")
    logger.critical("log level critical.")
