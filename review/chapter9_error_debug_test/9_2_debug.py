"""
@description: 错误、调试和测试：调试
@author     : wsl
@date       : 2024/12/30
"""
import logging


# 1. print()
# 最简单粗暴的方法是用print()把可能有问题的变量打印出来看看：
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n


# 2. assert 断言
# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
def foo2(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


# 3. logging
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
def foo3(s):
    n = int(s)
    logging.info('n = %d' % n)
    return 10 / n


logging.basicConfig(level=logging.INFO)
if __name__ == '__main__':
    # foo('0')
    # foo2('0')
    foo3('0')
