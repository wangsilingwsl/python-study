"""
@description: 面向对象高级编程：使用__slots__
@author     : wsl
@date       : 2024/12/27
"""
from types import MethodType


class Student(object):
    """
    正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
    """
    pass


class Student2(object):
    """
    如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
    为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
    """
    __slots__ = ('name', 'age')


if __name__ == '__main__':
    s = Student()
    # 然后，尝试给实例绑定一个属性：
    s.name = 'Michael'
    print(s.name)


    # 还可以尝试给实例绑定一个方法：
    def set_age(self, age):
        self.age = age


    s.set_age = MethodType(set_age, s)
    s.set_age(25)
    print(s.age)

    # 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
    s2 = Student()
    # s2.set_age(25)  # AttributeError: 'Student' object has no attribute 'set_age'

    # 使用__slots__
    s = Student2()
    s.name = 'Michael'
    s.age = 25
    # s.score = 99  # AttributeError: 'Student2' object has no attribute 'score'
