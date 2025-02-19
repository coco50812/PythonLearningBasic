"""
面向对象 =>
    类   =>  类是一类事物的统称,比如: 人,电脑,🍎,🍊,电视,平板.....
    对象  =>  对象一类事物当中具体的体现,比如: 张三,我现在使用的这台电脑,🌏
所有的类都有属性和方法
    属性 => (名词)  => def __init__(self):
        名字,鼻子,眼睛,性别,脚....
    方法 => (动词)
        吃饭,跳舞,说话....
定义一个类 => 使用定义类的关键字 class
比如:
    class Person(object):    # class是定义类的关键字,Person表示定义的类属于人类,object继承object(万事万物皆对象)
        # 属性
        # 方法

对象
    对象1 = 类名()
    对象2 = 类名()
    对象3 = 类名()
"""
class Person(object):
    # 属性 (姓名,年龄,性别)
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    # 方法 吃饭
    def eat(self):
        print("正在吃饭")

# 实例化对象
p1 = Person("张三",18,"男")
# 查看这个p1这个人的姓名
print(p1.name)
# 查看这个p1这个人的年龄
print(p1.age)
# 查看这个p2这个人的性别
print(p1.gender)
# 这个人还可以吃饭
p1.eat()


p2 = Person("李四",18,"女")
print(p2.name)
print(p2.age)
print(p2.gender)
p2.eat()







