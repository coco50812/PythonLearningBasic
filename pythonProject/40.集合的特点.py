"""
1. 可以将其他的数据类型转换成集合 set
2. 我们还有用我们数学里面的方法来对集合进行求并集,交集,差集
"""
a = {3,5}
print(a)
print(type(a))  # 他的数据类型 set

# 我们也可以将其他的数据类型转换成集合
a_set = set(range(8,14)) # 将range对象转换成集合,利用set来进行转换
print(a_set)
print(type(a_set))

# 我们还可以对列表进行转换成集合,并且有去重的功能
b_set = set([1,1,1,2,2,2,3,3,3,4])
print(b_set)

# 我们还可以对元祖进行转换成集合
c_set = set((1,2,3,1,2,3))
print(c_set)

# 还可以对字典进行转换成集合
d_set1 = set({"username":"张三","age":18})           #当直接对一个字典调用 set() 时，默认只迭代字典的键。
d_set2 = set({"username":"张三","age":18}.items())   #包含所有键值对
print(d_set1)
print(d_set2)



"""
我们使用数学的方法来对集合求并集,交集,差集
"""
e_set = set([1,2,3,4,5,6,7,8])
f_set = set([8,9,10,11,12,13])
print(e_set,f_set)

# 求e_set和f_set的并集 => |   , union
print(e_set | f_set)
print(e_set.union(f_set))

# 求e_set和f_set的交集 => & intersection
print(e_set & f_set)
print(e_set.intersection(f_set))

# 求e_set和f_set的差集
print(e_set.difference(f_set))
print(f_set-e_set)