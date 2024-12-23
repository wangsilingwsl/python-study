"""
@description: 面向对象编程：访问限制
@author     : wsl
@date       : 2024/12/23
"""


# class Student(object):
#     """
#     在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
#     但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性：
#     """
#
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))
#
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_score(self, score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('bad score')


class Student(object):
    """
    练习
    请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
    """

    def __init__(self, name, gender):
        self.name = name
        self.set_gender(gender)

    def get_gender(self):
        return self._gender

    def get_name(self):
        return self.name

    def set_gender(self, gender):
        if gender in ['male', 'female']:
            self._gender = gender
        else:
            raise ValueError("Invalid gender. Choose from'male' or 'female'.")


class Teacher(object):
    """
    @property装饰器就是负责把一个方法变成属性调用的：
    """

    @property
    def name(self, name):
        self.__name = name

    @property
    def gender(self, gender):
        self.__gender = gender

    @name.setter
    def name(self, name):
        self.__name = name


if __name__ == '__main__':
    bart = Student('Bart Simpson', 'male')
    print('姓名：%s，性别：%s' % (bart.get_name(), bart.get_gender()))
    """
    如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
    如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法：
    你也许会问，原先那种直接通过bart.score = 99也可以修改啊，为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数：
    """
    # bart.__name = 'New Name'  # 无法直接访问__name
    # print(bart.__name)  # New Name

    teacher1 = Teacher()
    teacher1.name = 'Selene'
    teacher1.gender = 'female'
    print('姓名：%s，性别：%s' % (teacher1.name, teacher1.gender))
    # 但是，如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
    # 如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法：
    # 你也许会问，原先那种直接通过bart.score = 99也可以修改啊，为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数：
    # bart.__name = 'New Name'  # 无法直接访问__name
    # print(bart.__name)  # New Name
    # 但是，外部代码还是可以自由地修改bart.__name或bart.__score：
    # 为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：
