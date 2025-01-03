"""
@description: IO编程：序列化
@author     : wsl
@date       : 2025/1/2
"""


def use_serialization():
    """
    在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：
    d = dict(name='Bob', age=20, score=88)
    可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。
    我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
    序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
    反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
    Python提供了pickle模块来实现序列化。
    首先，我们尝试把一个对象序列化并写入文件：
    """
