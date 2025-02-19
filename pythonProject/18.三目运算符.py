"""
三目运算符
    三目运算符也叫做三元运算符或者三元表达式
    语法:
        条件成立的时候执行这里面的代码 if 判断条件 else 当判断条件不成立的时候就执行这里的代码
"""
a = 1
b = 2
# c = a if a > b else b
# print(c)

c = a + b if a > b else a - b
print(c)