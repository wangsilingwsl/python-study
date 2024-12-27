"""
@description: 面向对象高级编程：使用元类
@author     : wsl
@date       : 2024/12/27
"""
from dataclasses import Field


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    """
    metaclass
    除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
    metaclass，直译为元类，简单的解释就是：
    当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
    但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
    连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
    所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
    metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。
    我们先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法：
    定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
    """

    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


if __name__ == '__main__':
    L = MyList()
    L.add(1)
    L.add(2)
    L.add(5)
    print(L)
