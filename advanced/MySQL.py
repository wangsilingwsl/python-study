"""
Python 操作MySQL数据库
Python 标准数据库接口为 Python DB-API，Python DB-API为开发人员提供了数据库应用编程接口。
Python 数据库接口支持非常多的数据库:
    GadFly mSQL MySQL PostgreSQL
    Microsoft SQL Server 2000
    Informix Interbase Oracle Sybase
可以访问 http://www.python.org/topics/database/DatabaseAPI-2.0.html 查看详细的支持列表。
    首先我们先要熟悉几个概念：
    数据库连接信息：包括服务器地址、端口号、用户名和密码等信息。
    数据库名：需要访问的数据库名，如runoob。
    表名：需要访问的表名。
    字段名：需要访问的字段名。
"""
"""
什么是MySQLdb?
MySQLdb 是用于Python链接Mysql数据库的接口,它实现了 Python 数据库 API 规范 V2.0，基于 MySQL C API 上建立的。
"""
import mysql.connector

# 创建连接
cnx = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="world"
)

# 创建游标
cursor = cnx.cursor()

# 执行查询
query = "SELECT * FROM city limit 10"
cursor.execute(query)

# 获取查询结果
results = cursor.fetchall()

# 打印结果
for row in results:
    print(row)

# 关闭游标和连接
cursor.close()
cnx.close()

"""
执行上面代码，如抛出异常raise errors.NotSupportedError(
mysql.connector.errors.NotSupportedError: Authentication plugin 'caching_sha2_password' is not supported
)
解决方法：
mysql-connector版本选择2.2.9
mysql-connector-python版本选择8.0.24
"""
