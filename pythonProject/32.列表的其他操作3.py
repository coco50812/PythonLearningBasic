"""
语法:
    len(list) => 获取列表当前的元素的个数(长度)
    max(list) => 获取列表当中元素的最大值
    min(list) => 获取列表当中元素的最小值
"""
list1 = [1,3,5,7,9]
# 获取列表的长度(个数)
print(len(list1))
# 获取元素当中的最大值
print(max(list1))
# 获取元素当中的最小值
print(min(list1))


"""
列表的方法
    list.append(obj) => 在列表的末尾添加一个元素
    list.count(obj) => 统计列表当中某一个元素的出现的次数
    list.extend(seq) => 将某一个序列添加到列表的最后面
    list.remove(obj) => 删除列表当中某一个匹配的元素
    list.reverse() => 翻转列表
    sorted => 对列表进行排序
        sorted(list) => 对列表进行从小到大的排序
        sorted(list,reverse=True) => 对列表进行从大到小的排序
"""
list2 = [1,3,5,7,9,2,4,6,8]
# 在列表的末尾添加一个元素
list2.append(2)
print(list2)

# 统计列表当中出现2的个数
print(list2.count(2))

# 将[1,1,1]这个序列添加到列表的末尾
list2.extend([1,1,1])
print(list2)

# 删除列表当中某一个匹配的元素,从前面往后面找,找到了那么就匹配,后面就不找了
list2.remove(2)
print(list2)

# 翻转列表
list2.reverse()
print(list2)

# 对列表进行排序
# 从小到大的排序
res1 = sorted(list2)
print(res1)
# 从大到小的排序
res2 = sorted(list2,reverse=True)
print(res2)
