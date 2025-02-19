"""
在python当中,我们在编写代码的过程当中,有时候,我们需要大量的工具包来赋值我们来进行开发
我们使用工具包:
    1. import ....
    2. from ... import ...
"""
# 案例一 => 使用random随机数
import random
print(random.randint(10,12))
print(random.choice(["🍎","🍊","🍌"]))

from random import randint
print(randint(1,3))



# 案例二 => 时间戳: 时间戳就是从1970年1月1日0时0分0秒开始计算
import time
print(time.time()) # 输出的结果就是从1970年1月1日0时0分0秒~现在我讲课的这个时间中间的所有毫秒值