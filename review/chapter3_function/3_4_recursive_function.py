"""
@description: 3_4_recursive_function 
@author     : wsl
@date       : 2024/12/19
"""


def recursive(n):
    """
    在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
    举个例子，我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：
    fact(n)=n!=1×2×3×⋅⋅⋅×(n−1)×n=(n−1)!×n=fact(n−1)×n
    所以，fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理。
    于是，fact(n)用递归的方式写出来就是：
    """
    if n == 1:
        return 1
    return n * recursive(n - 1)


def move(n, a, b, c):
    """
    练习
    汉诺塔的移动可以用递归函数非常简单地实现。
    请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
    """
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)  # 将前n-1个盘子从a借助c移动到b
        move(1, a, b, c)  # 将最底下的最后一个盘子从a移动到c
        move(n - 1, b, a, c)  # 将b上的n-1个盘子借助a移动到c


if __name__ == '__main__':
    print(recursive(5))
    print(recursive(100))

    # 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：
    # print(recursive(1000))

    move(3, 'A', 'B', 'C')
