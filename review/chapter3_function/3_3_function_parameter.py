"""
@description: 函数：函数的参数
@author     : wsl
@date       : 2024/12/19
"""


def power(x, n=2):
    """
    对于power(x)函数，参数n就是默认值2。这样，当我们调用power(5)时，相当于调用power(5, 2)：
    @param x: 底数
    @param n: 幂
    @return: x的n次方
    """
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 可变参数
def calc(*numbers):
    """
    在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
    我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
    要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
    @param numbers: 可变参数
    @return: sum
    """
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def keyword_param(name, age, **kw):
    """
    可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
    而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
    @param name: 名字
    @param age: 年龄
    @param kw: 关键字参数
    @return: name, age, kw
    """
    print('name:', name, 'age:', age, 'other:', kw)
    return name, age, kw


def func(a, b, c=0, *args, **kw):
    """
    参数组合
    在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
    但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
    @param a: 必选参数
    @param b: 必选参数
    @param c: 默认参数
    @param args: 可变参数
    @param kw: 关键字参数
    """
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def product(*args):
    """
    以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
    """
    if len(args) == 0:
        raise TypeError('请至少输入一个参数')
    else:
        sum = 1
        for n in args:
            sum = sum * n
        return sum

    # 测试
    print('product(5) =', product(5))
    print('product(5, 6) =', product(5, 6))
    print('product(5, 6, 7) =', product(5, 6, 7))
    print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
    if product(5) != 5:
        print('测试失败')
    elif product(5, 6) != 30:
        print('测试失败')
    elif product(5, 6, 7) != 210:
        print('测试失败')
    elif product(5, 6, 7, 9) != 1890:
        print('测试失败')
    else:
        print('测试成功')


def summary():
    """
    小结：
    1. 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
    2. 要注意定义可变参数和关键字参数的语法：
        *args是可变参数，args接收的是一个tuple；
        **kw是关键字参数，kw接收的是一个dict。
    3. 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
    4. 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
    5. 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
    6. 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
    7. 定义命名的关键字参数在没有可变参数的情况下不要忘记写分隔符*，否则定义的将是位置参数。
    """


if __name__ == '__main__':
    print(power(5))
    print(power(5, 2))
    print(calc(1, 2))
    keyword_param('wsl', 25)
    keyword_param('wsl', 25, city='beijing')
    keyword_param('wsl', 25, city='beijing', job='engineer')
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    keyword_param('wsl', 25, **extra)
    func(1, 2)
    func(1, 2, 3)
    func(1, 2, 3, 'a', 'b')
    func(1, 2, 3, 'a', 'b', x=99)
    # func(1, 2, 3, 'a', 'b', name='wsl')  # TypeError: func() got an unexpected keyword argument 'name'
    func(1, 2, 3, 'a', 'b', x=99, y=100)
    args = (1, 2, 3, 4)
    kw = {'x': 99, 'y': 100}
    func(*args, **kw)  # a = 1 b = 2 c = 3 args = (4,) kw = {'x': 99, 'y': 100}
    print(product(1, 2, 3, 4))
