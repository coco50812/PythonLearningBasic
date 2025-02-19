"""
super关键字就是子类用来调用父类的属性和方法的
"""
class Animal:
    def __init__(self,name):
        self.name = name

class Dog(Animal):# 继承动物类
    def __init__(self,name,can_guard):   #如果不重新定义这个可以，会默认继承父类init;但是既然def了，父init就会被完全覆盖 所以需要super简化代码
        # self.name = name  #功能简单 在这里和super实现功能是一样的
        # 我既然继承了父类,那么我是不是能少写一句,就少写一句,我使用父类当中的name,使用super关键字
        super().__init__(name) # 按住ctrl+键盘左键  继承父类中关于init的所有操作
        self.can_guard = can_guard

my_dog = Dog("旺财",True)
print(my_dog.name)
print(my_dog.can_guard)