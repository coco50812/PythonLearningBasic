"""
输入函数 => input
input是一个内置函数,可以用来获取用户的输入,返回的是一个字符串类型；都是在最后输入
内置 => 内置就是别人已经帮我们写好了,我们直接拿过来使用就可以了
"""
# 定义一个输入函数
age = input("请输入您的年龄")
print(age) # 得到的就是用户输入的年龄
print(type(age)) # 得到的是年龄,但是这个年龄是一个字符串类型

#输入多个值
age, height, name = input("请输入年龄、身高和名字（用空格分隔）：").split()
age = int(age)
height = float(height)
print(f"您好，{name}！您今年 {age} 岁，身高 {height:.2f} 米。")
