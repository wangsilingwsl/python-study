"""
面向对象编程
Python从设计之初就已经是一门面向对象的语言，正因为如此，在Python中创建一个类和对象是很容易的。

面向对象技术简介
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量, 用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
局部变量：定义在方法中的变量，只作用于当前实例的类。
实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：创建一个类的实例，类的具体对象。
方法：类中定义的函数。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
"""

"""
创建类。使用class 语句来创建一个新类，class 之后为类的名称并以冒号结尾:
class ClassName:
   '类的帮助信息'   #类文档字符串
   class_suite  #类体

empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。
第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
"""


class Employee:
    '所有员工的基类'  # 类文档字符串
    empCount = 0  # 类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


"""
self代表类的实例，而非类
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
"""


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()


# self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)


t = Test()
t.prt()

"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)
print(emp1.age)  # 获取新增属性的值
print(getattr(emp1, 'age'))  # 获取属性的值
print(hasattr(emp1, 'age'))  # 如果存在 'age' 属性返回 True。
setattr(emp1, 'age', 10)  # 添加属性 'age' 值为 8
print(getattr(emp1, 'age'))  # 获取属性的值
delattr(emp1, 'age')  # 删除属性 'age'
print(hasattr(emp1, 'age'))  # 如果存在 'age' 属性返回 True。

# Python内置类属性
print("Employee.__doc__:", Employee.__doc__)  # 类的文档字符串
print("Employee.__name__:", Employee.__name__)  # 类名
print("Employee.__module__:", Employee.__module__)  # 类定义所在的模块
print("Employee.__bases__:", Employee.__bases__)  # 类的所有父类构成元素（包含了一个由所有父类组成的元组）
print("Employee.__dict__:", Employee.__dict__)  # 类的属性（包含一个字典，由类的数据属性组成）


# Python对象销毁(垃圾回收)
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 析构函数
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")


pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))  # 打印对象的id
del pt1
del pt2
del pt3


# 类的继承
class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)


class Child(Parent):  # 定义子类
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print('调用子类方法')


c = Child()  # 实例化子类
c.childMethod()  # 调用子类的方法
c.parentMethod()  # 调用父类方法
c.setAttr(200)  # 再次调用父类的方法 - 设置属性值
c.getAttr()  # 再次调用父类的方法 - 获取属性值

# 使用issubclass()或者isinstance()方法来检测。
print(issubclass(Child, Parent))  # issubclass()方法来检测
print(isinstance(c, Child))  # isinstance()方法来检测


# 方法重写
class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法

"""
类属性与方法

类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。
在类内部的方法中使用时 self.__private_attrs。

类的方法
在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数
self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的。

类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 self.__private_methods

"""


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量

"""
单下划线、双下划线、头尾双下划线说明：
__foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
_foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import * 而导入。
__foo: 双下划线的表示的是私有类型(private)的变量，只能是允许这个类本身进行访问了。
"""
