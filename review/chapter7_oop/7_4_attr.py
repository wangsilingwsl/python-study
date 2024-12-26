"""
@description: 面向对象编程：属性
@author     : wsl
@date       : 2024/12/26
"""
import types


def use_type():
    """
    当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
    使用type()函数可以获取变量的类型，它返回一个Type对象。比如，判断一个对象是否是函数：
    """
    print(type(123))
    print(type('str'))
    print(type(None))

    # 如果一个变量指向函数或者类，也可以用type()判断：
    print(type(abs))

    # type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
    print(type(123) == type(456))
    print(type(123) == int)
    print(type('abc') == type('123'))
    print(type('abc') == str)
    print(type('abc') == type(123))

    # 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：

    def fn():
        pass

    print(type(fn) == types.FunctionType)
    print(type(abs) == types.BuiltinFunctionType)
    print(type(lambda x: x) == types.LambdaType)
    print(type((x for x in range(10))) == types.GeneratorType)


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Dog is eating...')


class Husky(Dog):
    def run(self):
        print('Husky is running...')


def use_instance():
    """
    对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
    我们回顾上次的例子，如果继承关系是：
    object -> Animal -> Dog -> Husky
    那么，isinstance()就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象：
    """
    a = Animal()
    d = Dog()
    h = Husky()

    print(isinstance(h, Husky))
    print(isinstance(h, Dog))
    print(isinstance(h, Animal))

    print(isinstance(d, Dog) and isinstance(d, Animal))
    print(isinstance(d, Husky))

    # 能用type()判断的基本类型也可以用isinstance()判断：
    print(isinstance('a', str))
    print(isinstance(123, int))
    print(isinstance(b'a', bytes))

    # 还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
    print(isinstance([1, 2, 3], (list, tuple)))
    print(isinstance((1, 2, 3), (list, tuple)))


def use_dir():
    """
    如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
    """
    print(dir('ABC'))

    # 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
    print(len('ABC'))
    print('ABC'.__len__())

    # 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
    class MyObject(object):
        def __init__(self):
            self.x = 9

        def power(self):
            return self.x * self.x

    obj = MyObject()
    print(hasattr(obj, 'x'))  # 有属性'x'吗？ True
    print(obj.x)
    print(hasattr(obj, 'y'))  # 有属性'y'吗？ False
    setattr(obj, 'y', 19)  # 设置一个属性'y' 19
    print(hasattr(obj, 'y'))  # 有属性'y'吗？ True
    print(getattr(obj, 'y'))  # 获取属性'y' 19
    print(obj.y)  # 获取属性'y' 19

    # 如果试图获取不存在的属性，会抛出AttributeError的错误：
    # getattr(obj, 'z')  # 获取属性'z'
    print(getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404

    # 也可以获得对象的方法：
    print(hasattr(obj, 'power'))  # 有方法'power'吗？
    print(getattr(obj, 'power'))  # 获取方法'power'
    fn = getattr(obj, 'power')  # 获取方法'power'
    print(fn())
    print(obj.power())


if __name__ == '__main__':
    use_type()
    use_instance()
    use_dir()
