"""
@description: 高级特性：切片
@author     : wsl
@date       : 2024/12/20
"""


def use_slice():
    """
    对经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
    """
    arrays = list(range(100))
    print(arrays)
    print(arrays[:10])  # 取前10个元素
    print(arrays[-10:])  # 取后10个元素
    print(arrays[10:20])  # 取第11-20个元素
    print(arrays[:10:2])  # 前10个数，每两个取一个
    print(arrays[::5])  # 所有数，每5个取一个
    print(arrays[:])  # 复制数组

    # tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
    t = (0, 1, 2, 3, 4, 5)
    print(t[:3])  # (0, 1, 2)

    # 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
    s = 'ABCDEFG'
    print(s[:3])  # 'ABC'


def trim(s):
    """
    练习
    利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
    """
    if s == '':
        return s
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


if __name__ == '__main__':
    use_slice()

    print(trim('hello  '))
    # 测试
    if trim('hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')
