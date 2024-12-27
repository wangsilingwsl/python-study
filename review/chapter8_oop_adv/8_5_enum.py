"""
@description: 面向对象高级编程：枚举类
@author     : wsl
@date       : 2024/12/27
"""

from enum import Enum, unique

# Enum，这是Python提供的一个枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


if __name__ == '__main__':
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

    for name, member in Weekday.__members__.items():
        print(name, '=>', member, ',', member.value)

    # 测试:
    bart = Student('Bart', Gender.Male)
    if bart.gender == Gender.Male:
        print('测试通过!')
    else:
        print('测试失败!')
