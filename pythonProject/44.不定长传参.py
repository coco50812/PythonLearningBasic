"""
不定长传参也叫做可变参数,当我们调用函数的时候,我们也不确定传递多少个参数,
当然也适用于不传参
注意: * 一个星号接收的参数是一个元祖
     ** 两个星号接收到的是一个字典
"""
def user_info1(*args): # * 号表示包裹位置参数
    print(args)
    print(f"我的名字叫做{args[0]},今年{args[1]}岁了,住在{args[2]}")
# 调用函数,传递参数
user_info1("张三",18,'北京')
#从键盘输入
user_input = input("请输入姓名、年龄和城市，用空格分隔：")
user_info1(*user_input.split())
# 其中*是解包操作符，params = ["张三", 18, "北京"]，user_info1(*params) 将一整个解包传给函数输入



def user_info2(** args): # * 号表示包裹关键子参数
    print(args)
    print(f'我的名字叫做{args["name"]},今年{args["age"]}岁了,住在{args["address"]}')
# 调用函数,传递参数
user_info2(name="刘祥",address="上海",age=25)