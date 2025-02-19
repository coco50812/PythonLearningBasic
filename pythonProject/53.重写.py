"""
重写 => 当父类里面继承下来的内容,不满足我要求的时候,我们需要将父类里面继承下来的内容给重写一份
"""
class Animal(object):
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(self.name+"吃")
class Dog(Animal): # 继承Animal
    # 当父类的里面的吃不满足我的要求的时候,那么我们需要对这个方法重写(重写写一遍)
    def eat(self,food):
        print(self.name+"吃"+food)

d = Dog("阿黄")
d.eat("狗粮")