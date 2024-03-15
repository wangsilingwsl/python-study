# Python 内置函数
# Python 内置了很多有用的函数，我们可以直接调用。

# abs()	返回数字的绝对值，如abs(-10) 返回 10
print("abs(-10) = ", abs(-10))

# all()	返回True,如果所有元素都为True
print("all([1,2,3,0]) = ", all([1, 2, 3, 0]))

# any()	返回True,如果任一元素为True
print("any([1,2,3,0]) = ", any([1, 2, 3, 0]))

# ord()	返回ASCII码
print("ascii('a') = ", ord('a'))

# bin()	将整数转换成二进制字符串
print("bin(10) = ", bin(10))

# bool()	转换为布尔类型
print("bool(0) = ", bool(0))

# bytearray()	返回一个新字节数组
print("bytearray(10) = ", bytearray(10))

# callable()	检查一个对象是否可调用
print("callable(print) = ", callable(print))

# chr()	返回整数对应的字符
print("chr(97) = ", chr(97))

# compile()	将字符串编译成python能识别或可执行的代码，也可以将文字读成字符串再编译。
print("compile('print(123)', '', 'exec') = ", compile('print(123)', '', 'exec'))

# complex()	创建一个复数
print("complex(1,2) = ", complex(1, 2))


# delattr()	删除对象的属性
class Coordinate:
    x = 10
    y = -5
    z = 0


point1 = Coordinate()  # 实例化一个类
print("x = ", point1.x)
print("y = ", point1.y)
print("z = ", point1.z)
delattr(Coordinate, 'z')  # 删除 z 属性
print("--删除 z 属性后--")
print("x = ", point1.x)
print("y = ", point1.y)
# print("z = ", point1.z)  # 会报错AttributeError，因为属性 z 已经被删除

# dict()	创建一个字典
numbers = dict(x=5, y=0)
print('numbers =', numbers)
print(type(numbers))

empty = dict()
print('empty =', empty)
print(type(empty))

# dir()	返回模块的属性列表
dir()  # 获得当前模块的属性列表
dir([])  # 查看列表的方法
