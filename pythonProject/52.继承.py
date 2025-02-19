"""
继承 => 继承子类将父类里面的内容给继承一份下来
"""
# 定义一个狗来
# class Dog(object): # 万事万物皆对象,就是所有的类都会自动的继承对象
#     def __init__(self,name):
#         self.name = name
#     def eat(self,food):
#         print(self.name+"吃"+food)
# dog = Dog("阿黄")
# dog.eat("狗粮")
#
# class chicken(object): # 万事万物皆对象,就是所有的类都会自动的继承对象
#     def __init__(self,name):
#         self.name = name
#     def eat(self,food):
#         print(self.name+"吃"+food)
# c = chicken("咯咯咯")
# c.eat("米")

# 我们就可以创建一个动物类,动物类有属性 name, 有方法 eat,然后让鸡和狗来继承一份动物来
class Animal(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print(self.name + "正在吃" + food)
# 创建一个狗来,让狗类来继承动物类
class Dog(Animal):
    pass # 保证代码结构的完整性
# 创建一个鸡类,让鸡类来继承动物类
class Chicken(Animal):
    pass

# 创建一个狗的对象
d = Dog("阿黄")
print(d.name)
d.eat("狗粮")


c = Chicken("咯咯咯")
print(c.name)
c.eat("米")
