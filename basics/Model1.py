"""
Python 模块
模块(Module)是一个Python文件，以.py结尾，包含了Python对象定义和Python语句。
模块让你能够有逻辑地组织你的Python代码段。
把相关的代码分配到一个模块里能让你的代码更好用，更易懂。
模块能定义函数，类和变量，模块里也能包含可执行的代码。
"""


def print_func(name):
    print("Model1 Hello : ", name)
    return


from package_runoob.runoob1 import runoob1
from package_runoob.runoob2 import runoob2

runoob1()
runoob2()
