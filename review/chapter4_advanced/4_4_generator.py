"""
@description: 高级特性：生成器
@author     : wsl
@date       : 2024/12/20
"""


def use_generator():
    """
    通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
    所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
    要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
    """
    numbers = [x * x for x in range(10)]
    print(numbers)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 通过生成器创建
    generator = (x * x for x in range(10))
    print(generator)  # <generator object use_generator.<locals>.<genexpr> at 0x0000026F1A4D7E40>

    # 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
    print(next(generator))  # 0
    print(next(generator))  # 1
    print(next(generator))  # 4
    print(next(generator))  # 9
    print(next(generator))  # 16
    print(next(generator))  # 25

    # 通过for循环来迭代generator
    for n in generator:
        print(n)


if __name__ == '__main__':
    use_generator()
