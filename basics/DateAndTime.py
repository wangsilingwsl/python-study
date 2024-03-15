"""
Python 日期和时间
Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。
Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
时间间隔是以秒为单位的浮点小数。
每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
Python 的 time 模块下有很多函数可以转换常见日期格式。
"""
import time

# 函数time.time()用于获取当前时间戳, 如下实例:

ticks = time.time()
print("当前时间戳为:", ticks)

"""
什么是时间元组？
很多Python函数用一个元组装起来的9组数字处理时间:
序号  字段	值
0	4位数年	2008
1	月	1 到 12
2	日	1到31
3	小时	0到23
4	分钟	0到59
5	秒	0到61 (60或61 是闰秒)
6	一周的第几日	0到6 (0是周一)
7	一年的第几日	1到366 (儒略历)
8	夏令时	-1, 0, 1, -1是决定是否为夏令时的旗帜

上述也就是struct_time元组。这种结构具有如下属性：

序号	属性	    值
0	tm_year	2008
1	tm_mon	1 到 12
2	tm_mday	1 到 31
3	tm_hour	0 到 23
4	tm_min	0 到 59
5	tm_sec	0 到 61 (60或61 是闰秒)
6	tm_wday	0到6 (0是周一)
7	tm_yday	1 到 366(儒略历)
8	tm_isdst	-1, 0, 1, -1是决定是否为夏令时的旗帜
"""
# 获取当前时间
localtime = time.localtime(time.time())
print("本地时间为:", localtime)

# 获取格式化的时间
localtime = time.asctime(time.localtime(time.time()))
print("格式化本地时间为:", localtime)

# 格式化日期
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取某月日历
# Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
import calendar

cal = calendar.month(2016, 1)
print("以下输出2016年1月份的日历:")
print(cal)
