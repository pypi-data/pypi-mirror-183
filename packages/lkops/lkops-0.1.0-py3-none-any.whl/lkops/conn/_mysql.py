# -*- encoding: utf-8 -*-
'''
@Time    :   2022-08-31 16:22:51
@Author  :   songhaoyang
@Version :   1.0
@Contact :   songhaoyanga@enn.cn
'''
import logging
import pymysql
import traceback
import pandas as pd
from urllib import parse
from dbutils.pooled_db import PooledDB
from sqlalchemy import create_engine, Table, MetaData


class MysqlConnector:
    def __init__(self, user, passwd, ip, port, db_name) -> None:
        """
        user: 用户名
        passwd: 密码
        ip: 目标ip
        port: mysql端口
        db_name: 目标库名
        """
        passwd = parse.quote_plus(passwd)
        self.url = f"mysql+pymysql://{user}:{passwd}@{ip}:{port}/{db_name}"
        self.engine = create_engine(self.url)
        self.metadata = MetaData(self.engine)
        self.connect = self.engine.connect()

    def reconnect(self):
        """
        mysql重连
        """
        self.engine = create_engine(self.url)
        self.metadata = MetaData(self.engine)
        self.connect = self.engine.connect()

    def insert(self, table_name, datas):
        """
        表插入接口
        table_name: 指定表名
        datas: 要插入的数据 形如 [{col1:d1, col2:d2}, {col1:d1, col2:d2}] 字段名和表列名保持一致
        """
        table_obj = Table(table_name, self.metadata, autoload=True)
        try:
            self.connect.execute(table_obj.insert(), datas)
        except Exception as error:
            try:
                self.reconnect()
                self.connect.execute(table_obj.insert(), datas)
            except Exception as error:
                print(error)
        finally:
            self.engine.dispose()
        print(table_name, '\tinsert ->\t', len(datas))

    def query(self, sql, orient="records"):
        """
        pd.read_sql_query
        sql: sql查询语句
        orient: 默认"orient" 返回的数据格式 [{col1:d1, col2:d2},{}]
        """
        try:
            res = pd.read_sql_query(sql, self.connect).to_dict(orient=orient)
        except Exception as error:
            try:
                self.reconnect()
                res = pd.read_sql_query(
                    sql, self.connect).to_dict(orient=orient)
            except Exception as error:
                print(error)
        finally:
            self.engine.dispose()
        return res

    def execute(self, sql):
        """
        执行sql语句
        """
        try:
            res = self.connect.execute(sql)
        except Exception as error:
            try:
                self.reconnect()
                res = self.connect.execute(sql)
            except Exception as error:
                print(error)
        finally:
            self.engine.dispose()
        return res


class MysqlDbPool():
    '''
    PooledDB() 参数含义

    creator：使用链接数据库的模块
    maxconnections：连接池允许的最大连接数，0和None表示没有限制
    mincached：初始化时，连接池至少创建的空闲的连接，0表示不创建
    maxcached：连接池空闲的最多连接数，0和None表示没有限制
    maxshared：连接池中最多共享的连接数量，0和None表示全部共享，ps:其实并没有什么用，因为pymsql和MySQLDB等模块中的threadsafety都为1，所有值无论设置多少，_maxcahed永远为0，所以永远是所有链接共享
    blocking：链接池中如果没有可用共享连接后，是否阻塞等待，True表示等待，False表示不等待然后报错
    setsession：开始会话前执行的命令列表
    ping：ping Mysql 服务端，检查服务是否可用
    '''

    def __init__(self, cfg) -> None:
        self.mysql_cfg = cfg
        self.pool = PooledDB(
            creator=pymysql,
            maxconnections=15,
            mincached=0,
            maxcached=20,
            maxshared=0,
            blocking=True,
            setsession=[],
            ping=5,
            host=self.mysql_cfg['ip'],
            port=self.mysql_cfg['port'],
            user=self.mysql_cfg['user'],
            password=self.mysql_cfg['passwd'],
            database=self.mysql_cfg['db_name'],
            charset='utf8mb4'
        )

    def execute(self, sql):
        # 使用连接池管理，每次获取连接，创建cursor
        # 执行sql, update/insert需要commit, select需要fetchall
        # 执行完毕后关闭连接，关闭游标
        res = None
        try:
            conn = self.pool.connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            res = cursor.fetchall()
        except Exception as error:
            logging.error("sql执行异常, msg=%s" % (repr(error)))
            logging.error(traceback.format_exc())
        finally:
            cursor.close()
            conn.close()
        return res


if __name__ == "__main__":
    # conn = MysqlConnector(user="root", passwd="qwe123", ip="localhost", port=3306, db_name="health_invention_db")
    # data = conn.query("select * from nutritious_food_health_tcm")
    # print(len(data))

    cfg = {
        'ip': '',
        'user': '',
        'passwd': '',
        'port': 3306,
        'db_name': ''
    }
    pool = MysqlDbPool(cfg)
    sql = "select * from table;"
    data = pool.execute(sql)
    print(data)
