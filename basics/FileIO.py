# 打印到屏幕
print("Python 是一个非常棒的语言，不是吗？")

"""
Python提供了两个内置函数从标准输入读入一行文本，默认的标准输入是键盘。如下：
input([prompt])：函数从标准输入读入一行文本，默认的标准输入是键盘。
raw_input([prompt])：函数从标准输入读入一行文本，并返回一个字符串（去掉结尾的换行符）：注意：python3.x中raw_input([prompt])函数被取消，而用input替换，其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。
"""
# str = input("请输入：")
# print("你输入的内容是: ", str)

# 打开一个文件
fo = open("writeFile.txt", "w")
fo.write("www.runoob.com!\nVery good site!\n")
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)

if not fo.closed:
    fo.close()

# read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。
fo = open("writeFile.txt", "r+")
str = fo.read()
print("读取的字符串是 : ", str)
position = fo.tell()
print("当前文件位置 : ", position)
if not fo.closed:
    fo.close()

# rename() 方法需要两个参数，当前的文件名和新文件名。
import os

os.rename("writeFile.txt", "writeFile3.txt")
os.remove("writeFile3.txt")
