"""
@description: IO编程：文件读写
@author     : wsl
@date       : 2024/12/31
"""


def file_read():
    """
    读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。
    读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
    """
    try:
        # encoding='utf-8'参数表示以utf-8编码读取文件，避免中文乱码
        f = open('10_0_io.py', 'r', encoding='utf-8')
        print(f.read())
    finally:
        if f:
            f.close()

    # 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
    with open('10_0_io.py', 'r', encoding='utf-8') as f:
        print(f.read())

    # 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
    with open('10_0_io.py', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            print(line.strip())  # 把末尾的'\n'删掉


def file_write():
    """
    写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
    """
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write('Hello, world!')
    # 你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：
    with open('test.txt', 'a', encoding='utf-8') as f:
        f.write('Hello, world!')


if __name__ == '__main__':
    file_read()
    file_write()
