"""
为什么要处理异常 => 当我们代码一旦报错之后
    1. 代码停止往后运行
    2. 出现的红色信息,给予用户不好友的提示
代码异常 =>
    try:
        # 在这里写你有可能会觉得出现异常的代码
    except 异常信息:
        # 当上面的代码出现了异常,那么就走这里
    else:
        # 当try里面代码没有出现异常,那么就走这里
    finally:
        # 无论上面的代码是否有异常出现,那么finally都会执行
人工异常
    raise ValueError("人为的抛出一个异常")
断言
    如果条件不成立,那么后续代码不再执行
"""
# 代码异常
try:
    # print(1 / 1)
    s = "None" # None不是字符串,没有长度
    print(len(s))
except ZeroDivisionError:
    print("0不能作为分母,不然就会报错")
except TypeError:
    print("类型错误")
else:
    print("代码OK,没有异常出现")
finally:
    print("不管有没有异常出现,他都执行这里")


# 人为异常
# raise：用于明确地抛出异常，无论在开发还是生产环境下，只要条件不满足，都希望程序停止并反馈错误信息。 有时候用软件抛出的异常就是raise
# score = 159
# if 100 >= score >= 0:
#     if score >= 60:
#         print("及格")
#     else:
#         print("不及格")
# else:
#     print("考试分数异常")
#     # 可以给他人为的抛出一个错误
#     raise ValueError("分数异常")    #后续代码无法运行 终止了


# 断言 => assert
print("程序开始")
# 语文和数学都超过了80分,我们就可以进行到下一轮的考试了
yuwen = 79
shuxue = 90
# if yuwen>=80 and shuxue >= 80:
#     print("可以进入到下一轮")
# else:
#     print("停止了")

# assert：用于在开发和调试阶段检查那些“永远不应该发生”的错误，如果条件不成立则说明代码内部存在问题。
assert yuwen>=80 and shuxue >= 80 ,"语文数学成绩都要大于80"# 如果说满足要求,那么就往后面走,如果没有满足的这个要求,那么终止了

print("直接进入到下一轮")
print("程序结束")
