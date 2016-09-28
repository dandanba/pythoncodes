# http://www.runoob.com/python3/python3-string.html
# Python 不支持单字符类型，单字符也在Python也是作为一个字符串使用。
from io import StringIO

char = 'c'
print(type(char))  # <class 'str'>

var1 = 'hello world!'
var2 = 'runoob'

print(var1[0])
print(var2[1:5])
out = StringIO()
for i in range(1, 5):
    out.write(str(i))
    out.write(", ")
out.seek(0)
print(list(var2), out.readlines())  # 从第二个到第五个
try:
    var1[0] = 'a'  # TypeError: 'str' object does not support item assignment
except TypeError as e:
    print(e)

print("已更新的字符串", var1[:6] + "Runoob")  # 从0开始取6个
print('a' in 'hello')  # False

a = "hello"
b = "python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if 'h' in a:  # __contains__
    print('h 在变量 a 中')
else:
    print('h 不在变量 a 中')

if 'm' not in b:  # __contains__
    print('m 不在变量 b 中')
else:
    print('m 在变量 b 中')

print(r"\n")
print(R"\n")

print('我叫%s今年%d岁' % ('wanggeng', 36))
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)

errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
# cursor.execute('''
# CREATE TABLE users (
# login VARCHAR(8),
# uid INTEGER,
# prid INTEGER)
# ''')

# Unicode 字符串
# 在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀 u。
# 在Python3中，所有的字符串都是Unicode字符串。

str1 = "wwwbaiducom1234567890"

print(str1.isalnum())  # S 字母和数字
print(str1.isalpha())  # S 字母

num = "1"
print(num, "num.isdigit()", num.isdigit())  # True
print(num, "num.isdecimal()", num.isdecimal())  # True
print(num, "num.isnumeric()", num.isnumeric())  # True

num = "Ⅷ"
print(num, "num.isdigit()", num.isdigit())  # False
print(num, "num.isdecimal()", num.isdecimal())  # False
print(num, "num.isnumeric()", num.isnumeric())  # True

# "〇","零","一","壱","二","弐","三","参","四","五","六","七","八","九","十","廿","卅","卌","百","千","万","万","亿"
num = "〇"
print(num, "num.isdigit()", num.isdigit())  # False
print(num, "num.isdecimal()", num.isdecimal())  # False
print(num, "num.isnumeric()", num.isnumeric())  # True

num = "四"  # 罗马数字
print(num, "num.isdigit()", num.isdigit())  # False
print(num, "num.isdecimal()", num.isdecimal())  # False
print(num, "num.isnumeric()", num.isnumeric())  # True

print(','.join(str1))

print(len(str1))
strl = str1.ljust(30, " ")
print(strl)
strr = str1.rjust(30, " ")
print(strr)
strc = str1.center(30, " ")
print(strc)

print(strl.rstrip())
print(strr.lstrip())
print(strc.strip())

print(str1.rjust(30, "0"))
print(str1.zfill(30))
