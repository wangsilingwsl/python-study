# 1.Hello world! - from DataFlair
print("Hello world! - from DataFlair")
print("hello");
print("world")

# 2.Variables - from DataFlair
print("Variables - from DataFlair")
a = 10
b = 20
print(a + b)

# 3.Operators - from DataFlair
print("Operators - from DataFlair")
a = 10
b = 20
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

# 4.Strings - from DataFlair
print("Strings - from DataFlair")
str1 = "Hello"
str2 = "World"
print(str1 + str2)
print(str1 * 3)
print(str1[0])
print(str1[1:4])

# 5.Lists - from DataFlair，列表，有序。列表中的元素可以修改。
print("Lists - from DataFlair")
list1 = [1, 2, 3, 4, 5]
print(list1)
print(list1[0])
print(list1[1:4])
list2 = ["Hello", "World"]
print(list2)
print(list2[0])
print(list2[1:4])

# 6.Tuples - from DataFlair，元组，类似于List，但是元组中的元素不能修改。
print("Tuples - from DataFlair")
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(tuple1[0])
print(tuple1[1:4])
tuple2 = ("Hello", "World")
print(tuple2)
print(tuple2[0])
print(tuple2[1:4])

# 7.Sets - from DataFlair
print("Sets - from DataFlair")
set1 = {1, 2, 3, 4, 5}
print(set1)
set2 = {1, 2, 3, 4, 5, 5, 5, 5}
print(set2)

# 8.Dictionaries - from DataFlair，字典。
# 除列表外Python最灵活的数据类型。两者区别是：列表中的元素是有序的，字典中的元素是无序的。字典中的元素是键值对的形式，键和值之间用冒号隔开，字典当中的元素是通过键来存取的，而不是通过偏移存取。
print("Dictionaries - from DataFlair")
dict1 = {1: "Hello", 2: "World"}
print(dict1)
print(dict1[1])
print(dict1[2])

# 9.Conditional Statements - from DataFlair
print("Conditional Statements - from DataFlair")
a = 10
b = 20
if a < b:
    print("a is greater than b")
else:
    print("b is greater than a")

# 10.Loops - from DataFlair
print("Loops - from DataFlair")
for i in range(1, 10):
    print(i)

# 11.Functions - from DataFlair
print("Functions - from DataFlair")


def add(a, b):
    return a + b


print(add(10, 20))

# 12.Classes and Objects - from DataFlair
print("Classes and Objects - from DataFlair")

# 13.File Handling - from DataFlair
print("File Handling - from DataFlair")
file = open("hello.txt", "w")
file.write("Hello World")
file.close()

# 注释
# 1.单行注释
# 我是单行注释
# 2.多行注释
'''
我是多行注释
'''
# 3.文档注释
"""
我是文档注释
"""

# 引号
# 1.单引号，表示一个单词
print('hello')
# 2.双引号，表示一个句子
print("hello world")
# 3.三引号，表示一个段落
print('''hello
hello 
world''')

# 变量
name = "张三"
print(name)
# 变量名的命名规则
# 1.变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头
# 2.变量名不能包含空格，但可使用下划线来分隔其中的单词
# 3.不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如print
# 4.变量名应既简短又具有描述性
# 5.慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0
miles = 1000.0
print(miles)

# 赋值整型变量
counter = 100
# 赋值浮点型变量
miles = 12000.0
print(counter)
print(miles)

# 多个变量赋值
a = b = c = 1
print(a, b, c)

# 多个对象指定多个变量
a, b, c = 1, 2, "john"
print(a, b, c)

# 数据类型转换
# 1.整型转换为浮点型
a = 1
print(float(a))
# 2.浮点型转换为整型
b = 1.0
print(int(b))
# 3.字符串转换为整型
c = "123"
print(int(c))
# 4.字符串转换为浮点型
d = "123.456"
print(float(d))
# 5.整型转换为字符串
e = 123
print(str(e))
# 6.浮点型转换为字符串
f = 123.456
print(str(f))
