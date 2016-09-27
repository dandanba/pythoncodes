# http://www.runoob.com/python3/python3-basic-syntax.html

# 第一个字符必须是字母表中字母或下划线'_'。
# 标识符的其他的部分有字母、数字和下划线组成。
# 标识符对大小写敏感。
# 在Python 3中，非-ASCII 标识符也是允许的了。
你好 = "你好"
print(你好)

import keyword

print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
# 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
# 'try', 'while', 'with', 'yield']

# 关键字 assert
assert True
# 关键字 del
list = [1, 2, 3, 4, 5, 6, 7, 8]

print("调用del list[0]前：", list)
del list[0]
print("调用del list[0]后：", list)
print("调用del list[2:3]前：", list)
print("list[2:3]", list[2:3])
del list[2:3]
print("调用del list[2:3]后：", list)

# 关键字 is
# is判断的是a对象是否就是b对象，是通过id来判断的
# ==判断的是a对象的值是否和b对象的值相等，是通过value来判断的
a = 100
b = 100.0
print("id(a)", id(a))
print("id(b)", id(b))
print("a==b", a == b)
print("a is b", a is b)  # print(id(a)==id(b))


# 关键字 lambda
# lambda函数也叫匿名函数，即，函数没有具体的名称,而用def创建的方法是有名称的。

# 不支持重载，使用默认的参数解决
# def foo():
#     return "lambda"

def foo(x=0, y=0):
    return "lambda" + str(x) + str(y)


f0 = lambda: "lambda"
f2 = lambda x, y: "lambda" + str(x) + str(y)
print(f0())
print(foo())
print(f2(1, 2))
print(foo(1, 2))

# 关键字 nonlocal

# 关键字 yield


if True:
    print("True")
else:
    print("False")

# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句
item1, item2, item3, item4 = 1, 2, 3, 4
print(item1 + \
      item2 + \
      item3 + \
      item4 \
      )

print(type(1))  # <class 'int'>
print(type(1.23))  # <class 'float'>
print(type(1 + 2j))  # <class 'complex'>

# 自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是换行。
print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(r"\n\n\n\n\n\n\n\n\n\n\n\n\n")
# python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。
print(u"this is an unicode string")
# 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
print("this""is""string")

word = "字符串"
sentence = "这是一个句子。"
paragraph = """
这是一个段落
"""
print(word)
print(sentence)
print(paragraph)

# http://www.cnblogs.com/weaming/p/5056492.html # python命名规范

input_name = input("请输入用户名：")
print("hello", input_name)

# 同一行显示多条语句
# import sys;x = 'runoob';sys.stdout.write(x + "\n")

a = 10
if a == 1:
    print(1)
elif a == 2:
    print(2)
elif a == 3:
    print(3)
else:
    print("other")

import sys

print(sys.argv)
# python python3-tutorial.py argv1 argv2 argv3
# ['python3-tutorial.py', 'argv1', 'argv2', 'argv3']
