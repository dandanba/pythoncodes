# http://www.runoob.com/python3/python3-list.html

# 序列都可以进行的操作包括索引，切片，加，乘，检查成员。
# 列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
# 列表的数据项不需要具有相同的类型

list1 = ['google', 'runood', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ['a', 'b', 'c', 'd']

print('list[0]:', list1[0])
print('list[1:5]:', list2[1:5])
print('第三个元素为：', list1[2])
list1[2] = 2001
print('更新后的第三个元素为：', list1[2])

print(list1)
del list1[2]
print('删除第三个元素：', list1)
list1.remove(2000)
print('删除 2000 后：', list1)

try:
    list1.remove(2000)
except ValueError as e:
    print(e)

# 列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
print(len([1, 2, 3, ]))
print([1, 2, 3, ] + [4, 5, 6, ])
print(['hi!'] * 4)
print(3 in [1, 2, 3])
for x in [1, 2, 3]:
    print(x)

L = ['google', 'runoob', 'taobao']
print(L[2])
print(L[-2])  # 最后一个是 -1
print(L[1:])
L1 = [1, 4, 9, 16, 25]
L2 = [36, 49, 64, 81, 100]
print(L1 + L2)

l1 = [1, 2, 3]
l2 = [3, 4, 5]
L = [l1, l2, l2]
print(L)
del l2[0]
print(L)

print(len(l1))
print(max(l1))
print(min(l1))
print(list('123'))

print(l1.append("1"))
print(l1)
print(l1.count(0), l1.count(1))

try:
    print(l1.index(0))
except ValueError as e:
    print(e)

l2 = l1.copy()
print(id(l2), id(l1))

L = [l1, l2]
print(L)
del l1[0]
print(L)
