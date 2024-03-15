"""
什么是异常？
异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。一般情况下，在Python无法正常处理程序时就会发生一个异常。异常是Python对象，表示一个错误。当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行。
"""

# 异常处理

try:
    fh = open("testfile.txt", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()


# 触发异常
# Python 使用 raise 语句抛出一个指定的异常。
def testRaise(level):
    if level < 1:
        raise Exception("Invalid level!", level)
    print("OK")


testRaise(1)
