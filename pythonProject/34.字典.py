"""
什么是字典 => 字典也是一组数据的集合,但是字典里面存储的是键值对的形式
    key_value
    人 => 张三
    猫 => 李四
    name => 张三
    age => gender
创建字典的时候,我们需要使用的 {}
"""
# 创建一个字典
"""
"username":"张三"
"age":18
"gender":"男"
"""
user_info = {"username":"张三","age":18,"gender":"男"}
print(user_info)

# 可以访问字符串里面的值,可以根据key获取到value
print("张三性别是 => ",user_info["gender"])
print("张三的年龄是 => ",user_info["age"])


# 字典里面的内容是可以被修改的,元祖是不能进行修改的
user_info["username"] = "文种玉"
user_info["gender"] = "女"
print(user_info)

# 删除字典的里面的元素,删除关键子 => del 字典[key]
del user_info["username"]
print(user_info)

# 清空字典 => 字典.clear()
user_info.clear()
print(user_info)

# 删除整个字典,删除的关键子 del 字典'
dict2 = {"username":"张三","age":18,"gender":"男"}
# 删除整个dict2这个字典
del dict2
# print(dict2) # 没有dict2这个字典了,就没有办法进行访问了