"""
@description: 面向对象高级编程：使用@property
@author     : wsl
@date       : 2024/12/27
"""


class Student(object):
    """
    在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改。
    这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，
    """

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


class Student2(object):
    """
    但是，上面的调用方法略显复杂，没有直接用属性这么直接简单。
    有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
    对于追求完美的Python程序员来说，这是必须要做到的！
    还记得装饰器（decorator）可以给函数动态加上功能吗？
    对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
    """

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # 只读属性。只定义getter方法，不定义setter方法就是一个只读属性：
    @property
    def birth(self):
        return self._birth


if __name__ == '__main__':
    s = Student()
    s.set_score(60)
    print(s.get_score())

    s2 = Student2()
    s2.score = 99
    print(s2.score)

    # 只读属性
    s2._birth = 1990
    print(s2.birth)
    # s2.birth = 2000  # AttributeError: can't set attribute
