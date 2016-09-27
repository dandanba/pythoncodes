# http://www.runoob.com/python3/python3-data-type.html
from runoob.python3.Data import Data

counter = 1000  # 整形变量
miles = 1000.0  # 浮点数
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)

a = b = c = 1
a, b, c, d = 1, 2, 3, 4  # 如果缺少了对应的字段那么会报错
# python3中包含六个基本的数据类型
# Number
#     int float bool complex 注意没有Long
# String
# List
# Tuple
# Sets
# Dictionary

a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
# <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>

# 注意：在Python2中是没有布尔型的，它用数字0表示False，用1表示True。
# 到Python3中，把True和False定义成关键字了，但它们的值还是1和0，它们可以和数字相加。
print(True + False + True)
print(1 is True)
print(0 is False)

var1 = 1
var2 = 2
del var1
del var2
# print(var1)  # NameError: name 'var1' is not defined
# del var1, var2  # NameError: name 'var1' is not defined

# data = Data()
# del data # 调用 __del__
# while True:
#     pass


print("5 + 4 = ", 5 + 4)
print("4.3 - 2 = ", 4.3 - 2)
print("3 * 7 = ", 3 * 7)
print("2 / 4 = ", 2 / 4)
print("2 // 4 = ", 2 // 4)
print("17 % 3 = ", 17 % 3)
print("2 ** 3 = ", 2 ** 3)

str1 = "Runoob"

print(str1)
print("str[0:-1]", str1[0:-1])
print("str[0]", str1[0])
print("str[2:5]", str1[2:5])
print("str[2:]", str1[2:])
print("str * 2", str1 * 2)
print(str1 + "Test")
# print(str - "Test")  # __sub__
# print(str / "Test")  # __div__
# print(str % "Test")  # __mod__
# ...

print("Run\noob")
print(r"Run\noob")

# str[1] = 'p'
# TypeError: 'str' object does not support item assignment

# 1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
# 2、字符串可以用+运算符连接在一起，用*运算符重复。
# 3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
# 4、Python中的字符串不能改变。

list1 = ['abc', 786, 2.23, 'runoob', 70.2]
tiny_list = [123, 'runoob']
print(list1)
print(list1[0])  # abc
print(list1[1:3])  # [786, 2.23]
print(list1[2:])  # [2.23, 'runoob', 70.2]
print(tiny_list * 2)  # [123, 'runoob', 123, 'runoob']
print(list1 + tiny_list)  # ['abc', 786, 2.23, 'runoob', 70.2, 123, 'runoob']

a = [1, 2, 3, 4, 5, 6, 7]
a[0] = 9
print(a)  # [9, 2, 3, 4, 5, 6, 7]
print(a[2:5])  # [3,4,5]

# 1、List写在方括号之间，元素用逗号隔开。
# 2、和字符串一样，list可以被索引和切片。
# 3、List可以使用+操作符进行拼接。
# 4、List中的元素是可以改变的。

tuple1 = ('abcd', 786, 2.23, 'runoob', 70.2)
tiny_tuple = (123, 'runoob')

print(tuple1)  # ('abcd', 786, 2.23, 'runoob', 70.2)
print(tuple1[0])  # abcd
print(tuple1[1:3])  # (786, 2.23)
print(tuple1[2:])  # (2.23, 'runoob', 70.2)
print(tiny_tuple * 2)  # (123, 'runoob', 123, 'runoob')
print(tuple1 + tiny_tuple)  # ('abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob')

tuple2 = (1, 2, 3, 4, 5, 6, 7)
# tuple[0] = 11
# TypeError: 'tuple2' object does not support item assignment
tuple3 = ()  # 空元组

# tuple4 = (4)
# print(tuple4) # 4
tuple4 = (4,)  # 一个元素，需要在元素后添加逗号
print(tuple4)

# 1、与字符串一样，元组的元素不能修改。
# 2、元组也可以被索引和切片，方法一样。
# 3、注意构造包含0或1个元素的元组的特殊语法规则。
# 4、元组也可以使用+操作符进行拼接。

student = {"Tom", "Jim", "Mary", "Tom", "Jack", "Rose"}
print(student)
if "Tom" in student:
    print("Tom 在集合中")
else:
    print("Tom 不集合中")

a = set("abracadabra")
b = set("alacazam")
la = list(a)
lb = list(b)
la.sort()
lb.sort()
print(la)
print(lb)
print("a - b ", a - b)  # 差集
print("a ^ b ", a ^ b)  # 不同时存在的元素
print("a & b ", a & b)  # 交集
print("a | b ", a | b)  # 合集

dict1 = {}
dict1['one'] = "1-菜鸟教程"
dict1[2] = "字典的关键字必须为不可变类型，且不能重复。"
dict1['two'] = "2-菜鸟工具"
tiny_dict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict1)
print(dict1['one'])
try:
    print(dict1[2])
except KeyError as e:
    print("KeyError: ", e)
print(tiny_dict)
print(tiny_dict.keys())
print(tiny_dict.values())

# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用 { }。


print(int(1.00))
# print(int("10.0"))  # ValueError: invalid literal for int() with base 10: '10.0'
print(int("1000"))

str1 = str(1000)
print(str1)
print(type(str1))
print()
print()
print()
print("repr() 将对象 x 转换为表达式字符串")
a = Data()
print(repr(a))  # 将对象 x 转换为表达式字符串
print("print('hello')->>>", 'hello')
print("print(repr('hello'))->>>", repr('hello'))
print()
print()
print()
print("用来计算在字符串中的有效Python表达式,并返回一个对象")
str_eval = "print('hello world')"
eval(str_eval)
list1 = [1, 3, 2, 4, ]
tuple1 = tuple(list1)
print(tuple1)

print(chr(20013))
print(ord('中'))
print(oct(20013))
print(hex(20013))
print(bin(20013))
