import Model1


def print_func(name):
    print("Model2 Hello : ", name)
    return


print_func("张三")
Model1.print_func("张三")

from Model3 import print_func
print_func("张三")

from math import *
print("math.pi = ", pi)
print("math.e = ", e)