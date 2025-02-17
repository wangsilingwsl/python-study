"""
@description: blog 
@author     : wsl
@date       : 2025/2/17
"""

from flask import Flask

# 创建 Flask 应用实例
blog = Flask(__name__)


@blog.route('/')
def hello_world():
    return 'Hello, World! This is blog!'


@blog.route('/name', methods=['POST'])
def my_name():
    return 'wsl \'s blog!'


if __name__ == '__main__':
    blog.run(debug=True)
