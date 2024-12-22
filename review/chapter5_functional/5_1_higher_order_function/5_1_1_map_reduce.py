"""
@description: 函数式编程：高阶函数：map/reduce
@author     : wsl
@date       : 2024/12/22
"""
from functools import reduce


def use_map():
    """
    map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
    """

    def f(x):
        return x * x

    r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(r))

    # map()传入的第一个参数是一个函数对象，使用lambda可以省略定义函数
    r = map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(r))

    # map()函数还可以接收两个以上的参数，当传入多个参数时，map()函数将依次作用到每个参数上
    def add(x, y):
        return x + y

    r = map(add, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(r))

    # 参数个数不等时，map()函数将以最短的序列为准
    r = map(add, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8])
    print(list(r))


def use_reduce():
    """
    reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
    """

    def add(x, y):
        return x + y

    r = reduce(add, [1, 3, 5, 7, 9])
    print(r)  # 25


def test():
    """
    利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
    """

    def normalize(name):
        return name.capitalize()

    l1 = ['adam', 'LISA', 'barT']
    l2 = list(map(normalize, l1))
    print(l2)

    # 利用reduce()函数，对list中的元素求积：
    def prod(x, y):
        return x * y

    r = reduce(prod, [2, 4, 5, 7, 12])
    print(r)


if __name__ == '__main__':
    use_map()
    use_reduce()
    test()
