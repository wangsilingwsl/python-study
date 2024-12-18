"""
@description: Python基础：模式匹配
@author     : wsl
@date       : 2024/12/18
"""


def match():
    """
    当我们用if ... elif ... elif ... else ...判断时，会写很长一串代码，可读性较差。
    如果要针对某个变量匹配若干种情况，可以使用match语句。
    例如，某个学生的成绩只能是A、B、C，用if语句编写如下：
    """
    score = 'B'
    if score == 'A':
        print('score is A.')
    elif score == 'B':
        print('score is B.')
    elif score == 'C':
        print('score is C.')
    else:
        print('invalid score.')

    # 使用match语句，可以更加简洁地表达这个逻辑：
    score = 'B'
    match score:
        case 'A':
            print('score is A.')
        case 'B':
            print('score is B.')
        case 'C':
            print('score is C.')
        case _:
            print('invalid score.')
    # 使用match语句时，我们依次用case xxx匹配，并且可以在最后（且仅能在最后）加一个case _表示“任意值”，代码较if ... elif ... else ...更易读。


# 复杂匹配
def complex_match():
    # match语句除了可以匹配简单的单个值外，还可以匹配多个值、匹配一定范围，并且把匹配后的值绑定到变量：
    age = 15

    match age:
        case x if x < 10:
            print(f'< 10 years old: {x}')
        case 10:
            print('10 years old.')
        case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
            print('11~18 years old.')
        case 19:
            print('19 years old.')
        case _:
            print('not sure.')  # case _表示其他所有情况
    # 在上面这个示例中，第一个case x if x < 10表示当age < 10成立时匹配，且赋值给变量x，第二个case 10仅匹配单个值，第三个case 11|12|...|18能匹配多个值，用|分隔。
    # 可见，match语句的case匹配非常灵活。


# 匹配列表
def match_list():
    # match语句还可以匹配列表，功能非常强大。
    # 我们假设用户输入了一个命令，用args = ['gcc', 'hello.c']存储，下面的代码演示了如何用match匹配来解析这个列表：
    args = ['gcc', 'hello.c', 'world.c']
    match args:
        # 如果仅出现gcc，报错:
        case ['gcc']:
            print('gcc: missing source file(s).')
        # 出现gcc，且至少指定了一个文件:
        case ['gcc', file1, *files]:
            print('gcc compile: ' + file1 + ', ' + ', '.join(files))
        # 仅出现clean:
        case ['clean']:
            print('clean')
        case _:
            print('invalid command.')


def test():
    """
    练习
    请用match语句编写一个简单的计算器，能够实现加减乘除运算。
    """
    match '1 + 2':
        case x:
            print(eval(x))
    match '3 - 4':
        case x:
            print(eval(x))
    match '5 * 6':
        case x:
            print(eval(x))
    match '8 / 2':
        case x:
            print(eval(x))


if __name__ == '__main__':
    match()
    complex_match()
    match_list()
    test()
