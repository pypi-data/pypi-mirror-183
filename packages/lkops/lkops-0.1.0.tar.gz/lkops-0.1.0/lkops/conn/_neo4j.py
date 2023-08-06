# -*- encoding: utf-8 -*-
'''
@Time    :   2022-08-31 16:47:39
@Author  :   songhaoyang
@Version :   1.0
@Contact :   songhaoyanga@enn.cn
'''
from py2neo import Graph
from tools.modules import clock
import sys
sys.path.append(".")


class GBConnector:
    def __init__(self, url, auth=("neo4j", "neo4j")) -> None:
        """
        url: 要创建的连接url 例 "http://0.0.0.0:7474"
        """
        self.url = url
        if auth:
            self.graph = Graph(url, auth=auth)
        else:
            self.graph = Graph(url)

    @clock
    def _run_cypher(self, cypher):
        """
        cypher: cypher查询语句
        """
        data = None
        try:
            data = self.graph.run(cypher).data()
        except Exception as e:
            try:
                self.graph = Graph(self.url)
                data = self.graph.run(data).data()
            except Exception as e:
                print(e)
        finally:
            if data:
                return data
            else:
                print("查询失败.")
                return None


if __name__ == "__main__":
    neo4j_connector = GBConnector(url="http://0.0.0.0:7474", auth=None)
    data = neo4j_connector._run_cypher(
        "MATCH (n) RETURN n.name as name, n.code as code")
    print(len(data))
