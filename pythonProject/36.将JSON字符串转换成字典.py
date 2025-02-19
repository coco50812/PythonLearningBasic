"""
将JSON字符串转换成字典
    1. 导入json工具包 => import json
    2. json.loads(JSON字符串)
"""
# 导入JSON工具包
import json
# 定义JSON字符串
data_json = '{"name":"张三","age":30,"city":"北京"}'
print(type(data_json))
# 将JSON字符串转换成字典
data_dict = json.loads(data_json)     #不一定是转换成dir 只是转换成python 然后里面内容是dir而已
print(data_dict)
print(type(data_dict))

# json.dumps将python=>json;json.loads 将json=>pthon