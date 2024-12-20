"""
@description: 高级特性：迭代
@author     : wsl
@date       : 2024/12/20
"""
from collections.abc import Iterable


def use_iterate():
    """
    如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
    在Python中，迭代是通过for ... in来完成的，而很多语言比如C或者Java，迭代list是通过下标完成的，比如Java代码：
    for (i=0; i<list.length; i++) {
        n = list[i];
    }
    可见，Python的for循环抽象程度要高于Java的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
    list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：
    """
    d = {'a': 1, 'b': 2, 'c': 3}
    for key in d:
        print(key)
    for value in d.values():
        print(value)
    for k, v in d.items():
        print(k, v)

    # 由于字符串也是可迭代对象，因此，也可以作用于for循环：
    for ch in 'ABC':
        print(ch)

    # 所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
    # 那么，如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断：
    print(isinstance('abc', Iterable))  # str是否可迭代：True
    print(isinstance([1, 2, 3], Iterable))  # list是否可迭代：True
    print(isinstance(123, Iterable))  # 整数是否可迭代：False

    # 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
    for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)

    # 上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
    for x, y in [(1, 1), (2, 4), (3, 9)]:
        print(x, y)


def test(numbers):
    """
    练习
    请使用迭代查找一个list中最小和最大值，并返回一个tuple：
    """
    if not isinstance(numbers, Iterable):
        raise TypeError('bad operand type')
    if len(numbers) == 0:
        return None, None
    min_num = max_num = numbers[0]
    for number in numbers:
        if number < min_num:
            min_num = number
        if number > max_num:
            max_num = number
    return min_num, max_num


if __name__ == '__main__':
    use_iterate()
    print(test([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # (0, 9)
