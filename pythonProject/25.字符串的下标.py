"""
字符串的下标(索引) => 都是从0开始
比如: str1 = Hello World
            01234567890
获取字符串当中对应下标的元素 => str1[n]
    n => 为0的时候表示的是获取下标(索引)为0的这个元素
    n => 为1的时候表示的是获取下标(索引)为1的这个元素
    n => 为2的时候表示的是获取下标(索引)为2的这个元素
    .. ..
"""
str1 = "我爱python"
#       0 1234567
print(str1)
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[7])
# print(str1[8]) out of range