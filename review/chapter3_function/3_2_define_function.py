"""
@description: 函数：定义函数
@author     : wsl
@date       : 2024/12/19
"""
import math


def my_abs(x):
    """
    在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
    我们以自定义一个求绝对值的my_abs函数为例：
    """
    if x >= 0:
        return x
    else:
        return -x


def nop():
    """
    如果想定义一个什么事也不做的空函数，可以用pass语句：
    pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
    """
    pass

    # pass还可以用在其他语句里，比如：
    # if age >= 18:
    #     pass


def check_param(x):
    """
    调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
    """
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x  # 将负数转换为正数


# 返回多个值
def move(x, y, step, angle=0):
    """
    函数可以返回多个值吗？答案是肯定的。
    比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的坐标：
    @return: nx 新的x坐标
    @return: ny 新的y坐标
    """

    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def test():
    """
    请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
    ax^2 + bx + c = 0 的两个解。
    提示：计算平方根可以调用math.sqrt()函数：
    """

    def quadratic(a, b, c):
        # 计算平方根
        delta = b * b - 4 * a * c
        if delta < 0:
            return None
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return x1, x2

    # 测试:
    print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
    print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

    if quadratic(2, 3, 1) != (-0.5, -1.0):
        print('测试失败')
    elif quadratic(1, 3, -4) != (1.0, -4.0):
        print('测试失败')
    else:
        print('测试成功')


def summary():
    """
    小结：
    1. 定义函数时，需要确定函数名和参数个数；
    2. 如果有必要，可以先对参数的数据类型做检查；
    3. 函数体内部可以用return随时返回函数结果；
    4. 函数执行完毕也没有return语句时，自动return None。
    5. 函数可以同时返回多个值，但其实就是一个tuple。
    """
    pass


if __name__ == '__main__':
    print(my_abs(-99))  # 99
    print(my_abs(99))  # 99
    nop()
    # check_param('A')  # TypeError: bad operand type
    print(check_param(99))  # 99
    print(check_param(-99))  # 99

    x, y = move(100, 100, 60, math.pi / 6)
    print(x, y)

    # 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
    r = move(100, 100, 60, math.pi / 6)
    print(r)  # (151.96152422706632, 70.0)

    test()
