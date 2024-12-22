"""
@description: 模块：安装第三方模块
@author     : wsl
@date       : 2024/12/22
"""
import sys

# 在Python中，安装第三方模块，是通过包管理工具pip完成的。
# 如果你正在使用Python 3，你应该已经有了pip，如果还没有安装，赶快去安装Python 3吧。
# 然后，可以在命令行下尝试运行pip：
# $ pip3 --version
# pip 18.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)
# 如果上述命令正常运行，说明pip已安装。

if __name__ == '__main__':
    for path in sys.path:
        print(path)
