"""
@description: 错误、调试和测试：错误处理
@author     : wsl
@date       : 2024/12/27
"""
from bdb import foo

if __name__ == '__main__':
    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally...')

    # 错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理。
    # 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
    try:
        print('try...')
        r = 10 / int('2')
        print('result:', r)
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
    else:
        print('no error!')
    finally:
        print('finally...')
    print('END')

    # Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：
    try:
        foo()
    except ValueError as e:
        print('ValueError')
    except UnicodeError as e:
        print('UnicodeError')
    except TypeError as e:
        print('TypeError')
