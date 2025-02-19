"""
将字典转换成JSON字符串
    1. 导入JSON工具(包) => import json,那么我们就可以使用json这个工具了
    2. 将字典转换成JSON紫都城 => json.jumps(字典,ensure_ascii=False)
"""
# 导入json的工具包
import json
# 定义一个字典,然后我们将字典转换成json字符串
data_dict = {
    "name":"张三",
    "age":30,
    "city":"长沙"
}
print(type(data_dict))
# 将字典转换成JSON字符串
# data_json = json.dumps(data_dict) # 他会将这个带有汉字的内容转换成Unicode编码格式
data_json = json.dumps(data_dict,ensure_ascii=False) # ensure_ascii=False固定写法,作用就是将汉字不转换
# 输出JSON子字符串
print(data_json)     #是str字符串了
# 查看是不是JSON字符串
print(type(data_json))