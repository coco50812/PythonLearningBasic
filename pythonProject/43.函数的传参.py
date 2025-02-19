"""
函数传参差不多可以分为四种情况
    1. 位置传参
    2. 关键词传参
    3. 默认参数
    4. 不定长传参
"""
# 1. 位置传参
def user_info1(name,age,address):
    print(f"我的名字叫做{name},今年{age}岁了,家住在{address}")
# 调用函数,使用的是位置传参
user_info1('张三',29,'长沙')

# 2. 关键词传参
def user_info2(name,age,address):
    print(f"我的名字叫做{name},今年{age}岁了,家住在{address}")
# 调用函数,使用的是关键子传参
user_info2(age=33,name='李四',address="巴黎")


# 3. 默认参数传参
def user_info3(name,age,gender='男'):
    print(f"我的名字叫做{name},今年{age}岁了,性别{gender}")
# 调用函数,使用的是默认参数,默认参数当我们传递了参数,那么就使用我们的,当我们没有传参的时候,那么就使用默认的
user_info3("王八",18,"女")
user_info3("刘九",28)