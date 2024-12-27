"""
@description: 面向对象高级编程：多重继承
@author     : wsl
@date       : 2024/12/27
"""
from socketserver import TCPServer, ForkingMixIn, UDPServer, ThreadingMixIn


class Animal(object):
    def run(self):
        print('Animal is running...')


class Mammal(Animal):
    def run(self):
        print('Mammal is running...')


class Bird(Animal):
    def run(self):
        print('Bird is running...')


class Dog(Mammal):
    def run(self):
        print('Dog is running...')


class Bat(Mammal):
    def run(self):
        print('Bat is running...')


class Parrot(Bird):
    def run(self):
        print('Parrot is running...')


class Ostrich(Bird):
    def run(self):
        print('Ostrich is running...')


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


class Dog2(Mammal, Runnable):
    pass


class Bat2(Mammal, Flyable):
    pass


class MyTCPServer(TCPServer, ForkingMixIn):
    pass


class MyUDPServer(UDPServer, ThreadingMixIn):
    pass


if __name__ == '__main__':
    dog = Dog()
    dog.run()

    bat = Bat()
    bat.run()

    parrot = Parrot()
    parrot.run()

    ostrich = Ostrich()
    ostrich.run()

    dog2 = Dog2()
    dog2.run()  # Mammal is running... 这里调用的是Mammal的run方法，而不是Runnable的run方法，因为多重继承是有顺序的，Mammal在前面，所以先调用Mammal的run方法

    bat2 = Bat2()
    bat2.run()
    bat2.fly()
