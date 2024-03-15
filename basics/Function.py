"""
Python 函数
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
函数能提高应用的模块性，和代码的重复利用率。
你已经知道Python提供了许多内建函数，比如print()。
但你也可以自己创建函数，这被叫做用户自定义函数。
"""
"""
定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
"""


# 定义函数
# 无参数
def printHello():
    print("hello")


printHello()


# 有参数
def printHelloWithName(name):
    print("hello ", name)


printHelloWithName("张三")


# 有返回值
def add(a, b):
    return a + b


print(add(1, 2))


# 任意参数
# 1.加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 2.而加**的参数会以字典的形式导入。
def printInfo(arg1, *vartuple):
    print("输出: ")
    print(arg1)
    print(vartuple)

    for var in vartuple:
        print(var)
    return


printInfo(10, 20, 30)


# 关键字参数
def printinfo(name, age=40):
    """打印任何传入的字符串"""
    print("Name: ", name)
    print("Age ", age)
    return


# 调用printinfo函数
printinfo(name="miki", age=50)
printinfo(name="siling")

"""
匿名函数
python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
lambda 只是一个表达式，函数体比 def 简单很多。
lambda 的主体是一个表达式，而不是一个代码块。
仅仅能在 lambda 表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
语法
lambda 函数的语法只包含一个语句，如下：
lambda [arg1 [,arg2,.....argn]]:expression
"""
# 如下实例：
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))

"""
return语句
return [表达式]语句用于退出函数，选择性地向调用方返回一个表达式。
不带参数值的return语句返回None。
之前我们看到的调用函数都没有向调用方返回数值，实际上，函数返回了None对象。
"""


def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


sum(10, 200)

"""
变量作用域
一个程序的所有的变量并不是在哪个位置都可以访问的。
访问权限决定于这个变量是在哪里赋值的。
变量的作用域决定了在哪一部分程序你可以访问哪个特定的变量名称。
两种最基本的变量作用域如下：
全局变量
局部变量
"""
total = 0  # 这是一个全局变量


def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


sum(10, 20)
print("函数外是全局变量 : ", total)

# dir()函数
# 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
import math
print(dir(math))