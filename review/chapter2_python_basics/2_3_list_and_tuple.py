"""
@description: Python基础：使用list和tuple
@author     : wsl
@date       : 2024/12/18
"""


def use_list():
    """
    Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
    比如，列出班里所有同学的名字，就可以用一个list表示：
    """
    print("----------list----------")
    classmates = ['Michael', 'Bob', 'Tracy']
    print(classmates)

    # 变量classmates就是一个list。用len()函数可以获得list元素的个数：
    print(len(classmates))

    # 用索引来访问list中每一个位置的元素，记得索引是从0开始的：
    print(classmates[0])
    print(classmates[1])
    print(classmates[2])
    # print(classmates[3])  # IndexError: list index out of range

    # 当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。
    print(classmates[-1])
    # 倒数第2个、倒数第3个：
    print(classmates[-2])
    print(classmates[-3])

    # list是一个可变的有序表，所以，可以往list中追加元素到末尾：
    classmates.append('Adam')
    print(classmates)

    # 也可以把元素插入到指定的位置，比如索引号为1的位置：
    classmates.insert(1, 'Jack')

    # 删除list末尾的元素，用pop()方法：
    classmates.pop()
    print(classmates)

    # 删除指定位置的元素，用pop(i)方法，其中i是索引位置：
    classmates.pop(1)
    print(classmates)

    # 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
    classmates[1] = 'Sarah'
    print(classmates)

    # list里面的元素的数据类型也可以不同，比如：
    types = ['Apple', 123, True]
    print(types)

    # list元素也可以是另一个list，比如：
    s = ['python', 'java', ['asp', 'php'], 'scheme']
    print(len(s))

    # 要注意s只有4个元素，其中s[2]又是一个list，如果拆开写就更容易理解了：
    p = ['asp', 'php']
    s = ['python', 'java', p, 'scheme']
    print(p)
    print(s)

    # 如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
    empty = []
    print(len(empty))


def use_tuple():
    """
    另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
    """
    print("----------tuple----------")
    classmates = ('Michael', 'Bob', 'Tracy')
    print(classmates)

    # 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
    # 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
    # tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来：
    t = (1, 2)
    print(t)

    # 如果要定义一个空的tuple，可以写成()：
    empty = ()
    print(empty)

    # 但是，要定义一个只有1个元素的tuple，如果你这么定义：
    t = (1)
    print(t)

    # 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
    # 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
    t = (1,)
    print(t)

    # 最后来看一个“可变的”tuple：
    t = ('a', 'b', ['A', 'B'])
    t[2][0] = 'X'
    t[2][1] = 'Y'
    print(t)
    # 这个tuple定义的时候有3个元素，分别是'a'，'b'和一个list。不是说tuple一旦定义后就不可变了吗？怎么后来又变了？
    # 别急，我们先看看定义的时候tuple包含的3个元素：
    # 指向'a'，指向'b'，指向list。
    # 后来list发生了变化：
    # 指向'a'，指向'b'，指向list的地址。
    # list的地址没有变，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
    # 理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。

    # 请看下面的代码：
    t = ('a', 'b', ('A', 'B'))
    print(t)  # 现在，对tuple的每个元素都是不可变的，即指向'a'，就不能改成指向'b'，指向'A'，就不能改成指向'X'，指向'B'，就不能改成指向'Y'，这样，tuple本身不变。


def test():
    """
    练习
    请用索引取出下面list的指定元素：
    """
    print("----------练习----------")
    array = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', 'Ruby', 'PHP'],
        ['Adam', 'Bart', 'Bob']
    ]

    # 打印Apple:
    print(array[0][0])
    # 打印Python:
    print(array[1][1])
    # 打印Bob:
    print(array[2][2])


if __name__ == '__main__':
    use_list()
    use_tuple()
    test()
