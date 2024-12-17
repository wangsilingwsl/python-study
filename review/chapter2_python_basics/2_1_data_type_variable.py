"""
@description: Python基础：数据类型和变量
@author     : wsl
@date       : 2024/12/17
"""


def data_type():
    """
    数据类型
    计算机顾名思义就是可以做数学计算的机器，因此，计算机程序理所当然地可以处理各种数值。但是，计算机能处理的远不止数值，还可以处理文本、图形、音频、视频、网页等各种各样的数据，不同的数据，需要定义不同的数据类型。在Python中，能够直接处理的数据类型有以下几种：
    """
    print("----------数据类型----------")
    # 整数
    # Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样，例如：1，100，-8080，0，等等。
    print(1, 100, -8080, 0)
    # 计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制用0x前缀和0 - 9，a - f表示，例如：0xff00，0xa5b4c3d2，等等。
    print(0xff00, 0xa5b4c3d2)
    # 对于很大的数，例如10000000000，很难数清楚0的个数。Python允许在数字中间以_分隔，因此，写成10_000_000_000和10000000000是完全一样的。十六进制数也可以写成0xa1b2_c3d4。
    print(10_000_000_000, 10000000000)

    # 浮点数
    # 浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，1.23x109和12.3x108是完全相等的。浮点数可以用数学写法，如1.23，3.14，-9.01，等等。但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5，等等。整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。
    print(1.23, 3.14, -9.01, 1.23e9, 12.3e8, 1.23e-5)

    # 字符串。是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等。请注意，''或""本身只是一种表示方式，不是字符串的一部分，因此，字符串'abc'只有a，b，c这3
    # 个字符。如果'本身也是一个字符，那就可以用""括起来，比如"I'm OK"包含的字符是I，'，m，空格，O，K这6个字符。 如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，比如：'I\'m
    # \"OK\"!'表示的字符串内容是：I'm "OK"!。
    print('abc', "xyz", "I'm OK", 'I\'m \"OK\"!', "I'm learning\nPython.")

    # 布尔值
    # 布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来：
    print(True, False)
    print(3 > 2, 3 > 5)
    print(True and True, True and False, False and False)

    # 空值
    print(None)


def variable():
    """
    变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。
    变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头
    """
    print("----------变量----------")
    # 比如：a，变量a是一个整数。可以直接计算a + 1：
    a = 1
    print(a)
    print(a + 1)

    # 变量a本身自增1后再赋值给变量c，然后打印c的值：
    a = a + 1
    c = a
    print(c)

    # 变量t_007是一个字符串。
    t_007 = 'T007'
    print(t_007)

    # 变量赋值
    a = 123
    b = a
    a = 'ABC'
    print(a, b)


PI = 3.14159265359
MAX_VALUE = 999999


def constant():
    """
    所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：
    """
    print("----------常量----------")
    print(PI)
    print(MAX_VALUE)


if __name__ == '__main__':
    data_type()
    variable()
    constant()