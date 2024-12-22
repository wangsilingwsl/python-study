"""
@description: 函数式编程：装饰器
装饰器是 Python 中一种很强大且有用的特性。
简单来说，装饰器就是一个函数，它可以用来修改其他函数的功能或行为。
@author     : wsl
@date       : 2024/12/22
"""


def now():
    print('2024-12-22')


# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数。
# 以下是一个简单的装饰器：
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
    print('2024-12-22')


if __name__ == '__main__':
    now()
    # 把@log放到now()函数的定义处，相当于执行了语句 now = log(now)
    # 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
    # wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
    # 在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
    # 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
