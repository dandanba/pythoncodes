# http://www.runoob.com/python3/python3-number.html
import math
from math import ceil, exp, fabs, floor, log, log10, modf, sqrt
from random import choice, randrange, random, shuffle, uniform

var1 = 1
var2 = 10
print(var1, var2)
try:
    del var1, var2
    print(var1, var2)  # NameError: name 'var1' is not defined
except NameError as e:
    print(e)

number = 0xA0F
print(number)
number = 0o037
print(number)

number = int("100")
print(number)
number = float("100")
print(number)
number = complex("100")
print(number)  # (100+0j)
number = complex(100, 1)
print(number)  # (100+1j)
# 在整数除法中，除法（/）总是返回一个浮点数，如果只想得到整数的结果，丢弃可能的分数部分，可以使用运算符 // ：
print(17 / 3)
print(17 // 3)
# print(aaa) #NameError: name 'aaa' is not defined
# 在交互模式中，最后被输出的表达式结果被赋值给变量 _ 。例如：
tax = 12.5 / 100
price = 100.5
_ = price * tax  # 在交互模式中，最后被输出的表达式结果被赋值给变量 _ 。
print(_)

# >>> tax = 12.5/100
# >>> price = 100.5
# >>> price * tax
# 12.5625
# >>> print(_)
# 12.5625


print(abs(-100))
print(ceil(4.1))
print(floor(-10.1))

# print(cmp(4, 3))# Python 3 已废弃 。使用 使用 (x>y)-(x<y) 替换。
x = "a"
y = "b"
print(x > y)  # __gt__
print(exp(2))
print(fabs(-10.0))
print(log(100, 10))
print(log10(100))
list1 = [100, 14, 13, 12, 11, 1000, 3, 3, 99, 4, 7, 5, 6]
print("max", list1, max(list1))
print("max", list1, max(100, 14, 13, 12, 11, 1000, 3, 3, 99, 4, 7, 5, 6))
print("min", list1, min(list1))
print("min", list1, min(100, 14, 13, 12, 11, 1000, 3, 3, 99, 4, 7, 5, 6))

print(modf(math.pi))  # (0.14150000000000018, 3.0)
print(pow(2, 2))
print(round(1 / 3, 3))  # 返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
print(sqrt(3))

print("choice:", choice(list1))
print("randrange(100):", randrange(100))
print("random:", int(random() * 100))

list1 = [1, 23, 12, 3123, 45241234, 6, 621231, 32123, 1231, 53463611, 3123]
print("before sort:", list1)
list1.sort()
print("after sort:", list1)
shuffle(list1)
print("after shuffle:", list1)
print("uniform:", uniform(1, 21))
""" 三角函数
acos(x)	返回x的反余弦弧度值。
asin(x)	返回x的反正弦弧度值。
atan(x)	返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	返回的x弧度的正弦值。
tan(x)	返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	将角度转换为弧度
"""
print("e", math.e)
