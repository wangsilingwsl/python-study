"""
@description: 面向对象编程：类和实例
面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
@author     : wsl
@date       : 2024/12/22
"""


class Student(object):
    """
    class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print('%s: %s' % (self.name, self.age))

    def judge_age(self):
        if self.age < 18:
            print('%s is a child.' % self.name)
        elif self.age < 60:
            print('%s is an adult.' % self.name)
        else:
            print('%s is an old.' % self.name)


if __name__ == '__main__':
    bart = Student('Bart Simpson', 61)
    print(bart)  # <__main__.Student object at xxxxxxxx>
    print(bart.name)  # Bart Simpson
    bart.print_info()
    bart.judge_age()

    selene = Student('Selene', 18)
    print(selene)  # <__main__.Student object at xxxxxxxx>
    selene.print_info()
    selene.judge_age()
