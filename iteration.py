# coding=utf-8
nfc = ["Packers", "49ers","a"]
afc = ["Ravens", "Patriots","b"]
bfc = ["Ravens", "Patriots","c"]
'''
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
'''
for teama, teamb,teamc in zip(nfc, afc,bfc):
    print(teama + " vs. " + teamb + " vv " + teamc)

'''
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
enumerate(sequence, [start=0])
sequence -- 一个序列、迭代器或其他支持迭代对象。
start -- 下标起始位置。
返回 enumerate(枚举) 对象。
'''
teams = ["Packers", "49ers", "Ravens", "Patriots"]
for index, team in enumerate(teams):
    print (index, team)


numbers = [1,2,3,4,5,6]
even = []
for number in numbers:
    if number%2 == 0:
        even.append(number)
print(even)

numbers = [1,2,3,4,5,6]
'''
列表解析
'''
even = [number for number in numbers if number%2 == 0]
print(even)

teams = ["Packers", "49ers", "Ravens", "Patriots"]
print({key: value for value, key in enumerate(teams)})

items = [0]*3
print (items)

'''
Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
str.join(sequence)
sequence -- 要连接的元素序列。
返回通过指定字符连接序列中元素后生成的新字符串。
'''
teams = ["Packers", "49ers", "Ravens", "Patriots"]
print (", ".join(teams))

data = {'user': 1, 'name': 'Max', 'three': 4,'admin':999}
try:
   is_admin = data['admin']
   print(is_admin)
except KeyError:
   is_admin = False
   print(is_admin)

'''
Python 字典 get() 函数返回指定键的值，如果值不在字典中返回默认值。
dict.get(key, default=None)
'''
data = {'user': 1, 'name': 'Max', 'three': 4,'admin':999}
is_admin = data.get('admin', False)
print(is_admin)

x = [1,2,3,4,5,6]
# 前3个
print (x[:3])
# 后三个
print(x[-3:])
# 中间四个
print(x[1:5])
# 奇数项
print(x[::2])
# 偶数项
print(x[1::2])

# print("**************************************")
# for x in range(101):print("fizz"[x%3*4::]+"buzz"[x%5*4::]or x)

from collections import Counter
print (Counter("hello"))

from itertools import combinations
teams = ["Packers", "49ers", "Ravens", "Patriots"]
for game in combinations(teams, 3):
    print(game)

