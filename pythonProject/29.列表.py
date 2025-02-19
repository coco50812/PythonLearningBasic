"""
列表 => 列表是一组数据的集合
列表的表示 => 用中括号表示 = []
比如: 我们班上40个人,如果我们要给班上的学生都要存储起来,那我们如果使用之前的变量,那么需要定义40个变量,这样的话足够麻烦
那么我们可以使用列表
举例:
    使用变量
        name1 = "张三"
        name2 = "李四"
        name3 = "网无"
    使用列表
        l = ["张三","李四","王五"]
"""
# 创建一个列表
# number_list = [1,3,5,7,9]
# # 可以搭配for in 循环使用,可以将number_list里面的元素一个一个的提取出来
# for item in number_list:
#     print(item)



# 可以访问列表当中的某一个元素 => [n] , 如果n为0,那么表示获取列表当中下标为0的元素
number_list = [1,3,5,7,9]
print(number_list[1])

# 还可以根据列表当中的下标更新列表当中的元素
number_list[1] = "王五"
print(number_list)


# 还可以删除列表当中的元素,del就是删除的意思 ！！！！
del number_list[3]
print(number_list)




