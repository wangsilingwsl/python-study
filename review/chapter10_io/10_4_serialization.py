"""
@description: IO编程：序列化
@author     : wsl
@date       : 2025/1/2
"""
import json
import pickle


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

    d = dict(name='Bob', age=20, score=88)
    print(d)
    pickle.dumps(d)
    # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。使用UTF-8编码写入：
    f = open('dump.txt', 'wb')
    pickle.dump(d, f)
    f.close()

    # 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
    f = open('dump.txt', 'rb')
    d = pickle.load(f)
    f.close()
    print(d)


def use_json():
    d = dict(name='Selene', age=20, score=88)
    print(d)
    json.dumps(d)  # json.dumps()方法返回一个str，内容就是标准的JSON。类似的，json.loads()方法可以把JSON字符串反序列化，变为Python对象：
    json_str = json.dumps(d)
    print(json_str)
    d = json.loads(json_str)
    print(d)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def json_advanced():
    s = Student('Bob', 20, 88)
    # print(json.dumps(s)) # TypeError: Object of type Student is not JSON serializable
    # 错误的原因是Student对象不是一个可序列化为JSON的对象。
    # 如果连class的实例对象都无法序列化为JSON，这肯定不合理！
    # 别急，我们仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数：
    # json.dumps(s, default=lambda obj: obj.__dict__)
    # 这样就可以把任意class的实例变为dict
    print(json.dumps(s, default=lambda obj: obj.__dict__))


def summary():
    """
    Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
    json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。

    1.序列化：把变量从内存中变成可存储或传输的过程称之为序列化。
    2.反序列化：把变量内容从序列化的对象重新读到内存里称之为反序列化。
    3.Python提供了pickle模块来实现序列化。
    4.使用pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
    5.使用pickle.load()方法从一个file-like Object中直接反序列化出对象。
    6.使用json.dumps()方法返回一个str，内容就是标准的JSON。
    7.使用json.loads()方法可以把JSON字符串反序列化，变为Python对象。
    8.如果连class的实例对象都无法序列化为JSON，可以使用json.dumps(s, default=lambda obj: obj.__dict__)把任意class的实例变为dict。
    """


if __name__ == '__main__':
    use_serialization()
    use_json()
    json_advanced()
