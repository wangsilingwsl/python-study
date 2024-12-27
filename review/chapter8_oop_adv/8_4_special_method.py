"""
@description: 面向对象高级编程：定制类、特殊方法
@author     : wsl
@date       : 2024/12/27
"""


class Student(object):
    """
    __str__
    直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
    也就是说，__repr__()是为调试服务的。
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for i in range(n):
                a, b = b, a + b
            return a


if __name__ == '__main__':
    student = Student('Michael')
    print(student)  # Student object (name: Michael)
    student  # Student object (name: Michael)

    for n in Fib():
        print(n)

    f = Fib()
    print(f[0])  # 1
    print(f[1])  # 1
    print(f[2])  # 2
    print(f[3])  # 3
    print(f[10])  # 89
    print(f[100])  # 573147844013817084101

    # 但是list有个神奇的切片方法：
    print(list(range(100))[5:10])  # [5, 6, 7, 8, 9]
