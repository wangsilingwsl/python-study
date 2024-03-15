"""
Python 算术运算符
以下假设变量： a=10，b=20：
运算符	描述	实例
+	加 - 两个对象相加	a + b 输出结果 30
-	减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -10
*	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 200
/	除 - x 除以 y	b / a 输出结果 2
%	取模 - 返回除法的余数	b % a 输出结果 0
**	幂 - 返回x的y次幂	a**b 为10的20次方， 输出结果 100000000000000000000
//	取整除 - 返回商的整数部分（向下取整）9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
"""
# Python 算术运算符实例
a = 10
b = 20
print("加：a + b = ", a + b)
print("减：a - b = ", a - b)
print("乘：a * b = ", a * b)
print("除：b / a = ", b / a)
print("取模：b % a = ", b % a)
print("幂：a ** b = ", a ** b)
print("取整除：9//2 = ", 9 // 2)

"""
Python 比较运算符
以下假设变量 a 为 10，变量 b 为 20：
运算符	描述	实例
==	等于 - 比较对象是否相等	(a == b) 返回 False。
!=	不等于 - 比较两个对象是否不相等	(a != b) 返回 true.
>	大于 - 返回x是否大于y	(a > b) 返回 False。
<	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。	(a < b) 返回 true。
>=	大于等于 - 返回x是否大于等于y。	(a >= b) 返回 False。
<=	小于等于 - 返回x是否小于等于y。	(a <= b) 返回 true。
"""
# Python 比较运算符实例
a = 10
b = 20
print("a = ", a)
print("b = ", b)
print("a == b = ", a == b)
print("a != b = ", a != b)
print("a > b = ", a > b)
print("a < b = ", a < b)
print("a >= b = ", a >= b)
print("a <= b = ", a <= b)

"""
Python 赋值运算符
以下假设变量 a 为 10，变量 b 为 20：
运算符	描述	实例
=	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
+=	加法赋值运算符	c += a 等效于 c = c + a
-=	减法赋值运算符	c -= a 等效于 c = c - a
*=	乘法赋值运算符	c *= a 等效于 c = c * a
/=	除法赋值运算符	c /= a 等效于 c = c / a
%=	取模赋值运算符	c %= a 等效于 c = c % a
**=	幂赋值运算符	c **= a 等效于 c = c ** a
//=	取整除赋值运算符	c //= a 等效于 c = c // a
"""
# Python 赋值运算符实例
a = 10
b = 20
c = 0
print("a = ", a)
print("b = ", b)
print("c = ", c)
c = a + b
print("c = a + b = ", c)
c += a
print("c += a = ", c)
c *= a
print("c *= a = ", c)
c /= a
print("c /= a = ", c)
c = 2
c %= a
print("c %= a = ", c)
c **= a
print("c **= a = ", c)
c //= a
print("c //= a = ", c)

"""
Python 位运算符
按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：
下表中变量 a 为 60，b 为 13二进制格式如下：
a = 0011 1100
b = 0000 1101
-----------------
a&b = 0000 1100
a|b = 0011 1101
a^b = 0011 0001
~a = 1100 0011
运算符	描述	实例
&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100
|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a | b) 输出结果 61 ，二进制解释： 0011 1101
^	按位异或运算符：当两对应的二进位相异时，结果为1 	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
~	按位取反运算符：对数据的每个二进制位取反，即把1变为0，把0变为1 	(~a ) 输出结果 -61 ，二进制解释： 1100 0011，在一个有符号二进制数的补码形式。
<<	左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000
>>	右移动运算符：把 ">>" 左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数	a >> 2 输出结果 15 ，二进制解释： 0000 1111
"""
# Python 位运算符实例
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0
print("a = ", a)
print("b = ", b)
print("c = ", c)
c = a & b
print("a & b = ", c)
c = a | b
print("a | b = ", c)
c = a ^ b
print("a ^ b = ", c)
c = ~a
print("~a = ", c)
c = a << 2
print("a << 2 = ", c)
c = a >> 2
print("a >> 2 = ", c)

"""
Python 逻辑运算符
Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:
运算符	逻辑表达式	描述	实例
and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
or	x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
"""
# Python 逻辑运算符实例
a = 10
b = 20
print("a = ", a)
print("b = ", b)
if (a and b):
    print("a and b = ", a and b)
else:
    print("a and b = ", False)
if (a or b):
    print("a or b = ", a or b)
else:
    print("a or b = ", False)
if not (a and b):
    print("not(a and b) = ", not (a and b))
else:
    print("not(a and b) = ", False)

tureFlag = True
falseFlag = False
print("tureFlag = ", tureFlag)
print("falseFlag = ", falseFlag)
if tureFlag and falseFlag:
    print("tureFlag and falseFlag = ", tureFlag and falseFlag)
else:
    print("tureFlag and falseFlag = ", False)

if tureFlag or falseFlag:
    print("tureFlag or falseFlag = ", tureFlag or falseFlag)
else:
    print("tureFlag or falseFlag = ", False)

if not (tureFlag and falseFlag):
    print("not(tureFlag and falseFlag) = ", not (tureFlag and falseFlag))
else:
    print("not(tureFlag and falseFlag) = ", False)

"""
Python 成员运算符
除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。
运算符	描述	实例
in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
"""
# Python 成员运算符实例
a = 10
b = 20
list = [1, 2, 3, 4, 5]
print("a = ", a)
print("b = ", b)
print("list = ", list)
if a in list:
    print("a 在 list 中")
else:
    print("a 不在 list 中")

if b not in list:
    print("b 不在 list 中")
else:
    print("b 在 list 中")

a = 2
if a in list:
    print("a 在 list 中")
else:
    print("a 不在 list 中")
