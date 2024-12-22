"""
@description: 函数式编程：偏函数
@author     : wsl
@date       : 2024/12/22
"""
import functools


def use_partial():
    """
    functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
    """

    int2 = functools.partial(int, base=2)
    print(int2('1000000'))  # 64
    print(int2('1010101'))  # 85

    # 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
    max2 = functools.partial(max, 10)
    print(max2(5, 6, 7))  # 10
    # 相当于：
    args = (10, 5, 6, 7)
    print(max(*args))  # 10
