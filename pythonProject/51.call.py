"""
当一个类的实例对象被调用的时候,那么就会自动的触发一个`call`这个方法的执行
"""


class Dog():  # 当我们在()里面不写object的时候,那么默认就有一个object存在
    def __init__(self, name):
        self.name = name

    # 定义一个call方法,当一个实例对象被调用了,那么就会自动的触发call方法的调用
    def __call__(self, x):
        print("我是call方法")
        # self.name => 阿黄 => 是一个字符串类型
        # "call" => 也是一个字符串类型
        # 1 => 是一个数字类型
        # 不能使用+号进行相加,如果+号的两边都是字符串,那么结果是拼接
        return self.name + "call" + x

    def eat(self):
        print(self.name + "正在吃")


dog = Dog("阿黄")
print(dog.name)
print(dog('1')) # () 的作用在调用就是执行


# 当我们给一个函数的名字添加一个() 的时候就会调用这个函数
# def fn():
#     print("我是一个函数")
#
# print(fn) # 这个输出fn 他指的就是内存当中的门牌号
# fn() # 当我们添加了一个（）之后,那么执行了这个函数



# print("阿黄"+1) # 字符串和数值不能进行使用+号
# print(1+1) # 数字和数字可以使用+号,那么这个+号的作用就是相加
# print("阿黄"+"咯咯咯") # 字符串可以和字符串进行相加,他们的作用就是拼接