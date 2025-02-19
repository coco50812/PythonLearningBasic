"""
for 循环的本质就是遍历"序列类型",但是range函数可以获取到一个简单的数字序列
    range(num) => 获取的就是从0~num(不包含num),比如:range(10),获取到的就是0~10,不包含10
    range(num1,num2) => 获取到就是从num1~num2(不包含num2),比如: range(1,10),获取到的就是1~10,不包10
    range(num1,num2,step) => 获取到就是从num1~num2(不包含num2),step就是步子,比如:range(1,10,3),获取到就是1,4,7
我们就可以使用range函数和forin循环搭配进行使用
"""
# 案例一
# 定义一个range函数
# res1 = range(10) # 0,1,2,3,4,5,6,7,8,9
# for i in res1:
#     print(i)


# 案例二
# 定义一个(1~10),不包含num2
# res2 = range(3,10)
# for item in res2:
#     print(item)


# 案例三
# res3 = range(1,10,4) # 1,5,9
# for item in res3:
#     print(item)