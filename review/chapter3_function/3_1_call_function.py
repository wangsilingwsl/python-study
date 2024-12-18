"""
@description: 函数：调用函数
@author     : wsl
@date       : 2024/12/18
"""


def function():
    """
    Python内置了很多有用的函数，我们可以直接调用。
    要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。可以直接从Python的官方网站查看文档，也可以在交互式命令行通过help(abs)查看abs函数的帮助信息。
    """

    # 调用abs函数：
    print(abs(100))  # 100
    print(abs(-20))  # 20
    print(abs(12.34))  # 12.34

    # max()函数可以接收任意多个参数，并返回最大的那个：
    print(max(1, 2))  # 2
    print(max(2, 3, 1, -5))  # 3

    # 数据类型转换
    print(int('123'))  # 123
    print(int(12.34))  # 12
    print(float('12.34'))  # 12.34
    print(str(1.23))  # '1.23'
    print(str(100))  # '100'
    print(bool(1))  # True
    print(bool(''))  # False


if __name__ == '__main__':
    function()
