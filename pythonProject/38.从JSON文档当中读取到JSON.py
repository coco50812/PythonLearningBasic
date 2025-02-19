"""
从JSON文件当中读取JSON
    1. 借助 json 工具包 => import json
    2. 从文件当中读取JSON字符串并转换成字典
        with open('data_json','r',encoding='utf-8') as f:
            data_dict = json.load(f)
            print(data_dict)
"""
# 导入json工具包
import json
# 从文档读取JSON字符串并且转换成字典
with open("data.json",'r',encoding='utf-8') as f:
    data_dict = json.load(f)
    print(data_dict)
    print(type(data_dict))