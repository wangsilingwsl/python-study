"""
@description: 函数式编程：高阶函数：sorted
@author     : wsl
@date       : 2024/12/22
"""


def use_sorted():
    """
    Python内置的sorted()函数就可以对list进行排序
    """
    l1 = [36, 5, -12, 9, -21]
    print(sorted(l1))  # [-21, -12, 5, 9, 36]

    # sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
    # key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
    print(sorted(l1, key=abs))  # [5, 9, -12, -21, 36]

    # 字符串排序
    l2 = ['bob', 'about', 'Zoo', 'Credit']
    print(sorted(l2))  # ['Credit', 'Zoo', 'about', 'bob']

    # 忽略大小写排序
    print(sorted(l2, key=str.lower))  # ['about', 'bob', 'Credit', 'Zoo']

    # 反向排序
    print(sorted(l2, key=str.lower, reverse=True))  # ['Zoo', 'Credit', 'bob', 'about']


if __name__ == '__main__':
    use_sorted()
