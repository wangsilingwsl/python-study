"""
@description: 函数式编程：lambda表达式
@author     : wsl
@date       : 2024/12/22
"""


def use_lambda():
    """
    Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。
    使用lambda表示匿名函数，冒号前面的x表示函数参数。
    """
    f = lambda x: x * x
    print(f(5))  # 25

    # 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
    # 此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
    f = lambda x, y: x + y
    print(f(1, 2))  # 3

    # 同样，也可以把匿名函数作为返回值返回
    def build(x, y):
        return lambda: x * x + y * y

    f = build(1, 2)
    print(f())  # 5

    # 在map()函数中使用匿名函数
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    l2 = list(map(lambda x: x * x, l1))
    print(l2)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]


def test():
    """
    请用匿名函数改造下面的代码：
    def is_odd(n):
        return n % 2 == 1

    L = list(filter(is_odd, range(1, 20)))

    print(L)
    """
    l = list(filter(lambda n: n % 2 == 1, range(1, 20)))
    print(l)


if __name__ == '__main__':
    use_lambda()
    test()
