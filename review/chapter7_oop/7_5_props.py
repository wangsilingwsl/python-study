"""
@description: 面向对象编程：实例属性和类属性
@author     : wsl
@date       : 2024/12/27
"""


class Student(object):
    """
    由于Python是动态语言，根据类创建的实例可以任意绑定属性。
    给实例绑定属性的方法是通过实例变量，或者通过self变量：
    """

    def __init__(self, name):
        self.name = name


class Student2(object):
    """
    但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
    """

    name = 'Student'


def summary():
    """
    实例属性属于各个实例所有，互不干扰；
    类属性属于类所有，所有实例共享一个属性。
    不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
    """
    pass


if __name__ == '__main__':
    # 给实例绑定属性
    s = Student('Bob')
    s.score = 90
    print(s.name)
    print(s.score)

    # 给类绑定属性
    s2 = Student2()
    print(s2.name)
