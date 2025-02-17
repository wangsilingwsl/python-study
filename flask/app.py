"""
@description: app 
@author     : wsl
@date       : 2025/2/17
"""

from flask import Flask

# 创建 Flask 应用实例
app = Flask(__name__)


# 定义路由和视图函数
@app.route('/')
def hello_world():
    return 'Hello, World!'


# post请求
@app.route('/post', methods=['POST'])
def my_name():
    return 'wsl'


if __name__ == '__main__':
    # 启动应用
    app.run(debug=True)
