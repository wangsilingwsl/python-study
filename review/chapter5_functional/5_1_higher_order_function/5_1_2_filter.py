"""
@description: 函数式编程：高阶函数：filter
@author     : wsl
@date       : 2024/12/22
"""


def use_filter():
    """
    Python内建的filter()函数用于过滤序列。
    和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
    """

    def is_odd(n):
        return n % 2 == 1

    r = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(r))

    # 把一个序列中的空字符串删掉
    def not_empty(s):
        return s and s.strip()

    r = filter(not_empty, ['A', '', 'B', None, 'C', '  '])
    print(list(r))

    # 用filter求素数
    def _odd_iter():
        n = 1
        while True:
            n = n + 2
            yield n

    gen = _odd_iter()
    for num in gen:
        if num < 100:
            print(num)
        else:
            break


if __name__ == '__main__':
    use_filter()
