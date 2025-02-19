"""
forin循环 => 在python语言当中,主要是用来遍历字符串,列表,range函数
语法:
    for 临时变量 in 字符串,列表,range函数:
        print(临时变量)
"""
# 案例一 => 将Python这个字符串里面的字母一个一个的遍历(循环)出来
for item in "Python":
    print(item)


# 案例二 => 将"小明跑了第三圈" 这个字符串一个一个的遍历出来
for i in "小明跑了第三圈":
    print(i)