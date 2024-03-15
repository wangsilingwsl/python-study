"""
Python 正则表达式
正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。
re 模块使 Python 语言拥有全部的正则表达式功能。
compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。
re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。
"""

import re

# re.match函数，尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
print(re.match('www', 'www.baidu.com').span())  # 在起始位置匹配
print(re.match('com', 'www.baidu.com'))  # 不在起始位置匹配

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

# re.search方法，扫描整个字符串并返回第一个成功的匹配。
print(re.search('www', 'www.baidu.com').span())  # 在起始位置匹配
print(re.search('com', 'www.baidu.com').span())  # 不在起始位置匹配

# re.sub用于替换字符串中的匹配项。
phone = "2004-959-559 # 这是一个电话号码"
# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)
# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)

# re.compile 函数，用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
print(m)
m = pattern.match('one12twothree34four', 2, 10)  # 从'e'的位置开始匹配，没有匹配
print(m)
m = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配
print(m)
print(m.group(0))  # 可省略 0
print(m.start(0))  # 可省略 0
print(m.end(0))  # 可省略 0
print(m.span(0))  # 可省略 0

# findall(string[, pos[, endpos]]) | re.findall(pattern, string[, flags])，搜索string，以列表形式返回全部能匹配的子串。
pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
print(result1)
print(result2)

# re.finditer(pattern, string, flags=0)，和findall类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())

# re.split(pattern, string[, maxsplit=0, flags=0]) | re.split(pattern, string[, maxsplit=0])，按照能够匹配的子串将字符串分割后返回列表。
print(re.split('\W+', 'runoob, runoob, runoob.'))
print(re.split('(\W+)', ' runoob, runoob, runoob.'))
print(re.split('\W+', ' runoob, runoob, runoob.', 1))
print(re.split('a*', 'hello world'))  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
print(re.split('(\W+)', ' runoob, runoob, runoob.', maxsplit=1))
print(re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE))
print(re.split('[a-f]+', '0a3B9'))
