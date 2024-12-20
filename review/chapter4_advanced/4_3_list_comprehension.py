"""
@description: 高级特性：列表生成式
@author     : wsl
@date       : 2024/12/20
"""
import os


def list_comprehension():
    """
    列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
    举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
    """
    print(list(range(1, 11)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
    numbers = []
    for x in range(1, 11):
        numbers.append(x * x)
    print(numbers)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # 但是循环太繁琐，而列表生成式可以用一行语句代替循环生成上面的list：
    print([x * x for x in range(1, 11)])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
    print([x * x for x in range(1, 11) if x % 2 == 0])  # [4, 16, 36, 64, 100]

    # 还可以使用两层循环，可以生成全排列：
    print([m + n for m in 'ABC' for n in 'XYZ'])  # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

    # 列出当前目录下的所有文件和目录名，可以通过一行代码实现：
    print([d for d in os.listdir('.')])

    # for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    print([k + '=' + v for k, v in d.items()])  # ['x=A', 'y=B', 'z=C']

    # 最后把一个list中所有的字符串变成小写：
    L = ['Hello', 'World', 'IBM', 'Apple']
    print([s.lower() for s in L])  # ['hello', 'world', 'ibm', 'apple']


def test():
    """
    练习
    请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
    """
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [s.lower() for s in L1 if isinstance(s, str)]
    print(L2)  # ['hello', 'world', 'apple']


if __name__ == '__main__':
    list_comprehension()
    test()
