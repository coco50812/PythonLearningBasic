"""
将数据写入到JSON字符串
    1. import json => 借助JSON的工具包
    2. with open("JSON数据","w,r,b",encoding="utf-8")) as f:
        json.dump(字典,f,ensure_ascii=False)
        关键子 =>
                with => 固定语法
                open => 打开JSON数据
                w,r,b  => (w => write => 写)   (r => read => 读)    (b => 二进制)
                encoding="utf-8" => 全球通用编码格式
                as => 取个小名,叫做 f
                ensure_ascii=False => 将汉字不进行编码
"""
# 借助工具包
import json
# 定义一个字典
data_dict = {
    "name":"CoCo",
    "age":30,
    "city":"长沙"
}
# 将字典转换成JSON字符串,并且写入文件当中
with open('data.json','w',encoding="utf-8") as f:
    json.dump(data_dict,f,ensure_ascii=False)









