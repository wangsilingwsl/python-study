"""
@description: 高级特性：迭代器
@author     : wsl
@date       : 2024/12/20
"""
from collections.abc import Iterable
from collections.abc import Iterator


def use_iterator():
    """
    我们已经知道，可以直接作用于for循环的数据类型有以下几种：
    一类是集合数据类型，如list、tuple、dict、set、str等；
    一类是generator，包括生成器和带yield的generator function。
    这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
    可以使用isinstance()判断一个对象是否是Iterable对象：
    """
    print(isinstance([], Iterable))  # list是否可迭代：True
    print(isinstance({}, Iterable))  # dict是否可迭代：True
    print(isinstance('abc', Iterable))  # str是否可迭代：True
    print(isinstance((x for x in range(10)), Iterable))  # generator是否可迭代：True

    # 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到没有元素时抛出StopIteration错误表示无法继续返回下一个值了。
    # 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
    # 可以使用isinstance()判断一个对象是否是Iterator对象：
    print(isinstance([], Iterator))  # list是否是迭代器：False
    print(isinstance({}, Iterator))  # dict是否是迭代器：False
    print(isinstance('abc', Iterator))  # str是否是迭代器：False
    print(isinstance((x for x in range(10)), Iterator))  # generator是否是迭代器：True

    # 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
    print(isinstance(iter([]), Iterator))  # list是否是迭代器：True
    print(isinstance(iter('abc'), Iterator))  # str是否是迭代器：True

    # 为什么list、dict、str等数据类型不是Iterator？
    # 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
    # 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
    # Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

    # 小结
    # 凡是可作用于for循环的对象都是Iterable类型；
    # 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
    # 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
    # Python的for循环本质上就是通过不断调用next()函数实现的，例如：
    for x in [1, 2, 3, 4, 5]:
        pass
    # 实际上完全等价于：
    # 首先获得Iterator对象：
    it = iter([1, 2, 3, 4, 5])
    # 循环：
    while True:
        try:
            # 获得下一个值：
            x = next(it)
        except StopIteration:
            # 遇到StopIteration就退出循环
            break


if __name__ == '__main__':
    use_iterator()
