"""
爬虫过程分析
当人类去访问一个网页时，是如何进行的？
1. 打开浏览器，输入网址，点击回车，浏览器向服务器发送请求。
2. 服务器接收到请求，处理请求，将处理结果返回给浏览器。
3. 浏览器接收到服务器返回的数据，并将数据显示在页面上。
4. 从网页中提取出我们需要的数据（文本、图片、视频等）。
5. 将提取出的数据保存到本地。

爬虫的过程也是如此，只不过爬虫是由程序来完成的。
1. 程序向服务器发送请求，请求获取指定的数据。
2. 服务器接收到请求，处理请求，将处理结果返回给程序。
3. 程序接收到服务器返回的数据，提取出需要的数据，对数据进行处理并保存。
"""
# 如何用Python请求一个网页？
# 1. 导入requests库 pip3 install requests
import requests

resp = requests.get('http://www.baidu.com')  # 向百度发起请求
print(resp)  # 打印请求结果的状态码
print(resp.content)  # 打印请求到的网页源码

# 2. 如何用Python解析网页源码？
# 导入BeautifulSoup库 pip3 install beautifulsoup4，pip3 install beautifulsoup4
from bs4 import BeautifulSoup

# 创建BeautifulSoup对象
soup = BeautifulSoup(resp.content, 'lxml')  # lxml是解析器，用于解析网页源码
print(soup.title)  # 打印网页标题
print(soup.title.text)  # 打印网页标题的文本
print(soup.prettify())  # 打印网页源码
a_list = soup.find_all('a')  # 获取网页中的所有a标签对象
text = ''  # 创建一个空字符串
for a in a_list:
    href = a.get('href')  # 获取a标签对象的href属性，即这个对象指向的链接地址
    text += href + '\n'  # 加入到字符串中，并换行
with open('baidu.txt', 'w') as f:
    f.write(text)  # 将字符串写入文件
