"""
在类当中,self是一个实例化对象,就是说谁创建了对象,那么这个self指的就是谁
"""
_self = "你好"
class Animal(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # 让这个_self等于self
        global _self
        _self = self
    def eat(self):
        print(self.name+"正在吃")

# 创建一个对象
dog = Animal("阿黄",2)
# # 我们刚刚有讲过,_self也就是self,也就是实例化对象dog,那么是不是就是说 dog
print(dog)
print(_self)
print(dog == _self)
# 我们来想一想
print(dog.name)
print(dog.age)
dog.eat()
chicken = Animal("咯咯咯",1)
print(chicken == _self)
print(dog == _self)
