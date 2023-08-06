# -*- encoding: utf-8 -*-
'''
@Time    :   2022-09-01 09:07:06
@Author  :   songhaoyang
@Version :   1.0
@Contact :   songhaoyanga@enn.cn
'''
import sys
sys.path.append(".")

from typing import List, Dict, AnyStr
from tools.modules import clock
from utils.Logger import Logging
from conn._neo4j import GBConnector


def init_or_add(lb_list: List[AnyStr] or AnyStr, di: Dict):
    if isinstance(lb_list, list):
        for lb in lb_list:
            if lb in di:
                di[lb] += 1
            else:
                di[lb] = 1
    elif isinstance(lb_list, str):
        lb = lb_list
        if lb in di:
            di[lb] += 1
        else:
            di[lb] = 1
    return di


@clock
def count_nodes(data):
    """
    统计指标:
    1. 节点数量
    2. 属性类目
    3. 属性总数量
    4. label类目
    5. 各label数量
    """
    attr_num = 0
    attr_class = set()
    label_class = set()
    label_count = dict()

    for i in data:
        [attr_class.add(j) for j in i['attr'].keys()]
        attr_num += len(i['attr'])
        [label_class.add(j) for j in i['label']]
        label_count = init_or_add(i['label'], label_count)

    print(f"节点数量:\t{len(data)}")
    print(f"属性类目:\t{len(attr_class)}")
    print(f"属性数量:\t{attr_num}")
    print(f"label类目:\t{len(label_class)}")
    print(f"label分布:\t{label_count}")
    return attr_num


@clock
def count_rels(data):
    """
    统计指标:
    1. 关系类目
    2. 关系总数
    3. 关系分布
    """
    rel_class = set()
    rel_dict = dict()
    for i in data:
        rel_dict = init_or_add(i['r'], rel_dict)
        rel_class.add(i['r'])
    print(f"关系总数:\t{len(data)}")
    print(f"关系类目:\t{len(rel_class)}")
    print(f"关系分布:\t{rel_dict}")
    return len(data)


@clock
def main(url, auth):
    conn = GBConnector(url, auth)
    nodes_data = conn._run_cypher(
        "MATCH (n) return n.name as name, properties(n) as attr, labels(n) as label")
    attr_num = count_nodes(nodes_data)
    rel_data = conn._run_cypher(
        "MATCH (h)-[r]->(t) return h.name as h, type(r) as r, t.name as t")
    rel_num = count_rels(rel_data)
    print(f"属性数+关系数共计(三元组数):{attr_num + rel_num}")


if __name__ == "__main__":
    url = "http://0.0.0.0:7474"
    # auth = (user, passwd)
    auth = None
    main(url, auth)
