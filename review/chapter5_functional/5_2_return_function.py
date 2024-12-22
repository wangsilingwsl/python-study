"""
@description: 函数式编程：返回函数
@author     : wsl
@date       : 2024/12/22
"""


def use_return_function():
    """
    高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
    我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
    """

    def calc_sum(*args):
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    # 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数
    def lazy_sum(*args):
        def sum():
            ax = 0
            for n in args:
                ax = ax + n
            return ax

        return sum

    # 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
    f = lazy_sum(1, 3, 5, 7, 9)
    print(f)  # <function lazy_sum.<locals>.sum at 0x0000021A4D6A7AF0>
    # 调用函数f时，才真正计算求和的结果
    print(f())  # 25

    # 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
    # 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
    # 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
    f1 = lazy_sum(1, 3, 5, 7, 9)
    f2 = lazy_sum(1, 3, 5, 7, 9)
    print(f1 == f2)  # False

    # 闭包
    # 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，
    # 其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
    # 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。
    # 我们来看一个例子：
    def count():
        fs = []
        for i in range(1, 4):
            def f():
                return i * i

            fs.append(f)
        return fs

    f1, f2, f3 = count()
    print(f1())  # 9
    print(f2())  # 9
    print(f3())  # 9

    # 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，
    # 因此最终结果为9。


def test():
    """
    利用闭包返回一个计数器函数，每次调用它返回递增整数：
    """

    def create_counter():
        def f(j):
            def counter():
                return j

            return counter

        fs = []
        for i in range(1, 4):
            fs.append(f(i))
        return fs

    c1, c2, c3 = create_counter()
    print(c1())  # 1
    print(c2())  # 2
    print(c3())  # 3


if __name__ == '__main__':
    use_return_function()
    test()
