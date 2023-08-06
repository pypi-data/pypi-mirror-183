# -*- encoding: utf-8 -*-
'''
@Time    :   2022-09-15 16:47:17
@Author  :   songhaoyang
@Version :   1.0
@Contact :   songhaoyanga@enn.cn
'''

from conn._neo4j import GBConnector
from collections import defaultdict
import yaml
import sys
sys.path.append(".")


def save_dict_to_yaml(dict_value: dict, save_path: str):
    """dict保存为yaml"""
    with open(save_path, 'w', encoding="utf-8") as file:
        file.write(yaml.dump(dict_value, allow_unicode=True))
    file.close()


def read_yaml_to_dict(yaml_path: str, ):
    with open(yaml_path, encoding="utf-8") as file:
        dict_value = yaml.load(file.read(), Loader=yaml.FullLoader)
    file.close()
    return dict_value


def main(url, auth):
    namespace = {"疾病": "disease", "食材": "ingredient", "食谱": "recipe"}
    conn = GBConnector(url, auth)
    data = {"nlu": []}
    nodes_data = conn._run_cypher(
        "MATCH (n) return n.name as name, n.名称 as _name, n.别名 as alias, labels(n) as label")
    classDict = defaultdict(list)
    for i in nodes_data:
        lb = i['label'][0]
        if lb == "食谱":
            classDict[lb] += [i['_name']]
        elif lb == "食材":
            classDict[lb] += [i['name']]
            alias = i['alias']
            if alias != "None":
                for alias_name in alias.split("，"):
                    classDict[lb] += [alias_name]
        else:
            classDict[lb] += [i['name']]
    [data['nlu'].append({"lookup": namespace.get(k), "example": v})
     for k, v in classDict.items() if namespace.get(k)]
    return data


if __name__ == "__main__":
    url = "http://0.0.0.0:7474"
    # auth = (user, passwd)
    auth = None
    res = main(url, auth)
    save_dict_to_yaml(res, "res.yml")
