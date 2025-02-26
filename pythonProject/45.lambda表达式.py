"""
lambda表达式的本质其实就是匿名函数,所谓匿名函数就是没有名字的函数
如果说一个函数只有一个返回值,并且只有一句代码,那么就可是用lambda表达式进行简化
简化 =>
    将def关键字进行去除,使用lambda进行替换,函数名也不需要,使用变量名来进行接收
    函数的参数的（）也给省略了,包括返回值return关键字也省略了
"""
# 普通函数
def fn1():
    return 100
# 调用函数
# res = fn1()
# print(res)
print(fn1()) # 等价代换


# lambda 匿名函数
fn1 = lambda : 100
print(fn1())