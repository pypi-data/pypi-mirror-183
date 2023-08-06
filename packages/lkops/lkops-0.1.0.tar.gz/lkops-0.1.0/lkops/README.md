# lk_ops

## statement

- The implementation of some open source **operators**, **modules** and **losses** is based on the principle of out of the box. 

- Each implementation should be attached with **application examples**, **sources** and **general principle descriptions**.

## structure

- conn
  - _redis.py: redis连接池示例
  - _mysql.py: 
    1. mysql单连接，查询，插入，更新，执行
    2. mysql连接池 执行
  - _neo4j.py: neo4j连接，执行cypher
- encode
  - relative_position_representation.py: torch相对位置编码
- tools
  - _threadpool.py: 线程池，异步机制
  - _count_neo4j.py: 图谱数据统计
  - _ecg_api_count.py: ecg调用统计
  - _export_kg_data_to_yml.py:: 导出图谱食材食谱数据到yml
  - modules.py: 计时装饰器, json number Encoder
- utils
  - Logger.py: devops logger配置


## Records
2022.11.07 14:03 update Logger.py
2022.11.09 17:52 定时任务
2022年12月26日18:14:01 更新发布方式
2022年12月27日18:15:31 poetry 测试

## release
### pypi auth

u: ticoAg

p: 19990523ONLY

### release command
1. 修改版本号
2. 执行
```shell
python setup.py bdist_wheel sdist
twine upload dist/* --verbose
```


注：具体用到的tool依赖需要在实际项目中声明安装，处于精简考虑 发布的lkops不做任何依赖绑定