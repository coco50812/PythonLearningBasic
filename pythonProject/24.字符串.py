"""
字符串 => "" 可以使用引号将一段字母,中文,数字包裹起来的,比如: "123","张三","男"...
字符串的分类
    1. 普通字符串 => 使用单引号或者双引号包裹起来,比如: "张三",'李四',"张三吃了'晚饭'"
    2. 模板字符串 => 使用三引号来进行表示,可以换行 ''' '''
    3. 纯数字字符串 => "123456789"
    4. 查询字符串 => 在传统的软件开发过程当中,前端可以往后端传入账号或者密码之类的内容,我们可以使用通过查询字符串进行吃传递
    5. JSON字符串 => 轻量级的数据交互格式,比如: '{"username":"张三","age":18,"gender":"男"}'
"""
# 1,2,3 => 普通字符串和纯数字字符串
str1 = "你好"
str2 = '我好'
str3 = "123465"
print(str1)
print(str2)
print(str3)

#
# 4. 查询字符串 => username=zhangsan&password=123456,他这个字符表示的username(账号)为zhangsan并且(&)password(密码)为123456
str4 = "username=zhangsan&password=123456"
print(str4)

# 如何从中提取username呢？
str5 = "username=zhangsan&password=123456&id=123"
pairs = str5.split('&')
params = {}
for pair in pairs:
    key, value = pair.split('=')
    params[key] = value

print(params['username'])


# 5. JSON字符串 可用内置的json模块提取username
import json

str6 = '{"username":"张三","age":18,"gender":"男"}'
data = json.loads(str6)
print(data['username'])
