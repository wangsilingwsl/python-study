"""
@description: 第一个Python程序：输入和输出
@author     : wsl
@date       : 2024/12/17
"""


# 输出
def test_output():
    # 用print()在括号中加上字符串，就可以向屏幕上输出指定的文字。比如输出'hello, world'
    print("hello world")

    # print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出。print()会依次打印每个字符串，遇到逗号“,”会输出一个空格
    print("The quick brown fox", "jumps over", "the lazy dog")

    # print()也可以打印整数，或者计算结果
    print(300)
    print(100 + 200)


# 输入
def test_input():
    # input()函数可以让用户输入字符串，并存放到一个变量里
    name = input()
    print(name)

    # input()可以传入一个字符串，这个字符串将作为提示信息
    name = input('please enter your name: ')
    print('hello,', name)


# 练习
# 请利用print()输出1024 * 768 = xxx：
def test():
    print('1024 * 768 =', 1024 * 768)


# 程序主入口
if __name__ == '__main__':
    # test_output()
    # test_input()
    test()
