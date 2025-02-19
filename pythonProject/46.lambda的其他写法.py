# 带普通参数的lambda表达式
fn1 = lambda a,b : a + b
print(fn1(1,2))


# 带包裹参数的lambda表示
fn2 = lambda *args:args
print(fn2(10,20,30))


# 带包裹关键词的lambda表达式
fn3 = lambda **kwargs:kwargs
print(fn3(name="张三",age=20))


# 带有默认参数的lambda表达式
fn4 = lambda a,b,c = 100 : a+b+c
print(fn4(20,40))