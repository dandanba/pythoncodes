# http://www.runoob.com/python3/python3-basic-operators.html
a = 21
b = 10
c = 0

c = a + b
print('1 - c 的值为：', c)
c = a - b
print('2 - c 的值为：', c)
c = a * b
print('3 - c 的值为：', c)
c = a / b
print('4 - c 的值为：', c)
c = a % b
print('5 - c 的值为：', c)
# 修改变量 a 、b 、c
a = 10
b = 5
c = a ** b
print('6 - c 的值为：', c)
a = 10
b = 5
c = a // b
print('7 - c 的值为：', c)

a = 21
b = 10
c = 0
if a == b:
    print('1 - a 等于 b')
else:
    print('1 - a 不等于 b')

if a != b:
    print('2 - a 不等于 b')
else:
    print('2 - a 等于 b')

if a < b:
    print('3 - a 小于 b')
else:
    print('3 - a 大于 b')

if a > b:
    print('4 - a 大于 b')
else:
    print('4 - a 小于 b')

if a <= b:
    print('5 - a 小于等于 b')
else:
    print('5 - a 大于等于 b')

if a >= b:
    print('6 - a 大于等于 b')
else:
    print('6 - a 小于等于 b')

a = 21
b = 10
c = 0
c = a + b
print("1 - c 的值为：", c)
c += a
print("2 - c 的值为：", c)
c *= a
print("3 - c 的值为：", c)
c /= a
print("4 - c 的值为：", c)

c = 2
c %= a
print("5 - c 的值为：", c)

c **= a
print("6 - c 的值为：", c)

c //= a
print("7 - c 的值为：", c)

a = 60  # 0011 1100
b = 13  # 0000 1101
c = 0
print(bin(a)[2:])
print(bin(b)[2:])
c = a & b
print('1 - c 的值为：', c, bin(c)[2:])
c = a | b
print('2 - c 的值为：', c, bin(c)[2:])
c = a ^ b
print('3 - c 的值为：', c, bin(c)[2:])
c = ~a
print('4 - c 的值为：', c, bin(c)[3:])
c = a << 2
print('5 - c 的值为：', c, bin(c)[2:])
c = a >> 2
print('6 - c 的值为：', c, bin(c)[2:])

a = 10
b = 20
if a and b:
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if a or b:
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为true")
else:
    print("2 - 变量 a 和 b 都不为 true")

a = 0
if a and b:
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if a or b:
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为true")
else:
    print("4 - 变量 a 和 b 都不为 true")

if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")

a = 10
b = 20
list1 = [1, 2, 3, 4, 5, 6, 7]
if a in list1:
    print("1 - 变量 a 在给定的列表 list中")
else:
    print("1 - 变量 a 不在给定的列表 list中")

if a not in list1:
    print("2 - 变量 a 不在给定的列表 list中")
else:
    print("2 - 变量 a 在给定的列表 list中")
a = 3
if a in list1:
    print("3 - 变量 a 在给定的列表 list中")
else:
    print("3 - 变量 a 不在给定的列表 list中")

a = 20
b = 20
# Python身份运算符
if a is b:
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")
if id(a) == id(b):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")

b = 30
if a is b:
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if a is not b:
    print("4 - a 和 b 有相同的标识")
else:
    print("4 - a 和 b 没有相同的标识")

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d
print("(a + b) * c / d 的运算结果为：", e)

e = ((a + b) * c) / d
print("((a + b) * c) / d 的运算结果为：", e)

e = (a + b) * (c / d)
print("(a + b) * (c / d) 的运算结果为：", e)

e = a + (b * c) / d
print("a + (b * c) / d 的运算结果为：", e)
