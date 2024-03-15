"""
Python OS 文件/目录方法
Python 的os模块提供了帮你执行文件处理操作的方法，比如重命名和删除文件。
要使用这个模块，你必须先导入它，然后才可以调用相关的各种功能。
"""
import os

# 检验权限模式
if os.access("./", os.F_OK):
    print("F_OK - 返回值 %s" % os.F_OK)
else:
    print("F_OK - 没有读取权限")

# 改变当前工作目录
os.chdir("./")
print("当前工作目录为 %s" % os.getcwd())

# 判断目录是否存在
if os.path.exists("./test"):
    print("目录存在")
else:
    # 创建目录
    os.mkdir("./test")

# 删除目录
os.rmdir("./test")
