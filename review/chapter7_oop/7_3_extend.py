"""
@description: 面向对象编程：继承和多态
@author     : wsl
@date       : 2024/12/26
"""


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Dog is eating...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')

    def eat(self):
        print('Cat is eating...')


if __name__ == '__main__':
    dog = Dog()
    dog.run()
    dog.eat()

    cat = Cat()
    cat.run()
    cat.eat()

    # 多态。当我们定义一个class的时候，我们实际上就定义了一种数据类型。我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样：
    a = list()  # a是list类型
    b = Animal()  # b是Animal类型
    c = Dog()  # c是Dog类型
    print(isinstance(a, list))
    print(isinstance(b, Animal))
    print(isinstance(c, Dog))

    # 看上去a、b、c确实对应着list、Animal、Dog这3种类型。但是等等，试试：
    print(isinstance(c, Animal))


    # 看来c不仅仅是Dog，c还是Animal！
    # 不过仔细想想，这是有道理的，因为Dog是从Animal继承下来的，当我们创建了一个Dog的实例c时，我们认为c的数据类型是Dog没错，但c同时也是Animal也没错，Dog本来就是Animal的一种！
    # 所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行：
    # print(isinstance(b, Dog))
    # Dog可以看成Animal，但Animal不可以看成Dog。
    # 要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量：
    def run_twice(animal):
        animal.run()
        animal.run()


    # 当我们传入Animal的实例时，run_twice()就打印出：
    run_twice(Animal())
    # 当我们传入Dog的实例时，run_twice()就打印出：
    run_twice(Dog())
    # 当我们传入Cat的实例时，run_twice()就打印出：
    run_twice(Cat())
