"""
逻辑运算符
    与   and
    或   or
    非   not

    True and True   => True
    True and False  => False
    False and True  => False
    False and False => False
        当与运算的时候,只有and两边都为true的时候,那么结果才为true,否则为false

    True or True    => True
    True or False   => True
    False or True   => True
    False or False  => False
        当或运算的时候,只有or的两边都为false的时候,那么结果为false,否则就为True

    not True    => False
    not False   => True
        非真既假,非假既真
"""
print(10 > 20 and 10 < 20)
print(20 > 10 and 20 == 20)

print(10 > 20 or 10 < 20)
print(10 > 20 or 10 == 20)

print(not (10 > 20))
print(not (20 == 20))
