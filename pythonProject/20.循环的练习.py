"""
1. 练习1 => 死循环,所谓的死循环当while后面的条件为True的时候,那么他会永远的执行下去
while True:
    # 这里面的循环就会永远的执行下去
"""
# while 20>10:
#     print("这个是一个死循环")



"""
利用循环来1~100之间的和
"""

sum=0
for i in range(1,101):
    sum=sum+i
print(sum)

# sum = 0 # 这个变量就是用来求和的
# index = 0 # 这个变量就用循环的初始化的值
# while index <= 100:
#     sum += index # sum = sum + index
#     print(index,sum)
#     # 记录循环的次数,每循环一次,我们都需要添加一个1
#     index += 1



"""
求1~100之间的偶数和
"""
result=0
for i in range(1,101):
    if i%2==0:
        result=result+i
print(result)



# sum = 0
# index = 1
# while index <= 100:
#     # 如果index是偶数,那么我们就把index累加进来
#     if index % 2 == 0:
#         # print(index)
#         sum += index
#     index += 1
#
# print(sum)
