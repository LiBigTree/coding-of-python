
# 字典——一种映射的数据结构， 可以理解为序列的索引不在是数字，而可以是数、字符等等

# 1、创建字典  项（item）：键>值
print('1:')
x = {'one': '1', 'two': '2'}
print(x)

# 2、dict
print('2:')
items = [('name', 'Gumby'), ('age', '42')]
d = dict(items)
print(d)

# 字典基本操作
# 字典很多地方都类似于序列
# len(d) 项的数
# d[k]: 返回与键k相关的值， 联想索引
# d[k] = v 将值v关联到键k， 联想赋值
# del d[k] 删除键为k的项
# k in d 字典是否包含键为k的项 ， 联想成员资格检查
# 字典可以自动添加不存在的项，如果赋值的话 （列表就不可以，可以理解：毕竟字典是无序的，列表是有序的）

# ---使用实例---
# 思考键值对应一个键延申最多几层？ 出于对代码可读性的考虑，一般对应到两层
# people = {
#     'Alice': {'phone': '2341', 'addr': 'Foo drive 23', 'hobby': 'reading'},
#     'Beth': {'phone': '9102', 'addr': 'Bar street 42', 'hobby': 'reading'},
#     'Ceil': {'phone': '3158', 'addr': 'Baz avenue 90', 'hobby': 'reading'}
# }
#
# # 当一个键对应多个值时，应考虑描述性的标签
# labels = {
#     'phone': 'phone number',
#     'addr': 'address',
#     'hobby': 'hobby'
# }
#
# name = input('Name: ')
#
# request = input('phone number(p) or address(a) or h: ')
#
# if request == 'p': key = 'phone'
# if request == 'a': key = 'addr'
# if request == 'h': key = 'hobby'
#
# if name in people: print("{}'s {} is {}.".format(name, labels[key], people[name][key]))
# # -----------------------------------------------------------------------------------------
# people = {
#     'Alice': {'phone': '2341', 'addr': 'Foo drive 23', 'hobby': {0: 'reading', '1': 'sleep'}}
# }
#
# print(people['Alice']['hobby'][0])
# 感悟： 字典的键值索引可以是数（整数、浮点数）、字符串、元组

# --------------------2020年1月15日学习-------------------------
# # 创建一个变量保存名字的四种方法
# name = '李德'
#
# # 拼串
# print('欢迎 ' + name + ' 光临！')
# # 多个参数
# print('欢迎', name, '光临！')
# # 占位符
# print('欢迎 %s 光临！' % name)
# # 格式化字符串
# print(f'欢迎 {name} 光临！')

# ------2020年1月16日学习------------------------
# 数据元素 —— 数值 字符串 空值
# a = -5//2
# print(a)
# b = 5//2
# print(b)
# 通过上面，知道python中整除是向坐标轴左边圆整。同时，在未来的使用过程也应该常注意 正负号不同带来的影响

# ----2020/02/02---
# 3、字符串格式设置功能用于字典----
print('3: ')
phone_book = {'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'}
print("Ceil's phone number is {Cecil}".format_map(phone_book))

# ----------字---典---方---法------------------

# 4、clear 清除所有的字典项
print('4:')
d = {'age': 42, 'name': 'Gumby'}
returned_value = d.clear()
print(d)
print(returned_value)

# 案例:
# 场景一：
print('4.1:')
x = {}
y = x
x['key'] = 'value'
print(y)
x = {}
print(y)  # 场景一x的变化没有对y产生影响
# 场景二：
print('4.2:')
x = {}
y = x
x['key'] = 'value'
print(y)

print(x.clear())
print(y)
# 场景二用方法后 都被清除了

# 解释： 场景一创造了一个新字典关联到x，而y仍然指向原来的字典
# 场景二clear是针对原字典，直接做了清除

# 5、copy 浅复制：当修改副本值，原件也会变化  可以看出 这种复制是 复制了键，没复制值
# （这里有点迷 暂且这样 待以后学到更多原理再探究佐证）
print('5:')
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'] .remove('bar')
print(y)
print(x)
# >> 深复制——复制所有的值
from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')

print(c)
print(dc)

# 6、fromkeys 创建一个新字典，其中包含指定的键
print('6:')
print(dict.fromkeys(['name', 'age'], '(unknown)'))

# 7、get 用其访问字典时，不会引发异常，而是返回一个值，默认是None，也可指定
print('7:')
d = {}
print(d.get('name', 'N/A'))
d['name'] = 'Eric'
print(d.get('name'))

# ------2020年1月19日 对字典实例思考----------------
#
# people = {
#     'Alice': {'phone': '2341', 'addr': 'Foo drive 23', 'hobby': 'reading'},
#     'Beth': {'phone': '9102', 'addr': 'Bar street 42', 'hobby': 'reading'},
#     'Ceil': {'phone': '3158', 'addr': 'Baz avenue 90', 'hobby': 'reading'}
# }
#
# # 当一个键对应多个值时，应考虑描述性的标签
# labels = {
#     'phone': 'phone number',
#     'addr': 'address',
#     'hobby': 'hobby'
# }
#
# name = input('Name: ')
#
# request = input('phone number(p) or address(a) or hobby(h): ')
#
# # 如果做数据库，这里还需要考虑用户输入错的key怎么办 然后如何引导正确输入
# if request == 'p':
#     key = 'phone'
#     label = labels.get(key)
#     result = people.get(name, 'not available')
#     print("{}'s {} is {}.".format(name, label, result[key]))
#
# elif request == 'a':
#     key = 'addr'
#     label = labels.get(key)
#     result = people.get(name, 'not available')
#     print("{}'s {} is {}.".format(name, label, result[key]))
#
# elif request == 'h':
#     key = 'hobby'
#     label = labels.get(key)
#     result = people.get(name, 'not available')
#     print("{}'s {} is {}.".format(name, label, result[key]))
#
# else:
#     print('数据查询项不存在')

# 8、items 返回一个包含所有字典项的列表—— 字典视图（key, value）
print('8:')
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
it = d.items()
print(it)

# 字典视图：可用于迭代，可确定长度，可成员资格检查
# 字典视图不复制，始终是底层字典的反映
d['spam'] = 1
print(('spam', 0) in it)
print(('spam', 1) in it)

# 9、keys 返回一个键的字典视图
print('9:')
print(d.keys())

# 10、values 返回一个由字典中的值组成的字典视图
print('10: ')
print(d.values())

# 11、pop 获取指定键关联的值并将之删除
print('11: ')
d = {'x': 1, 'y': 2}
print(d.pop('x'))
print(d)

# 12、popitem 随机弹出一个字典项并将之删除
print('12: ')
print(d.popitem())

# 13、setdefault 获取与指定键相关联的值而且当不包含指定值的键时，在字典中添加指定的值和键
# 联想get的功能
print('13: ')
d = {}
d.setdefault('name', 'N/A')
print(d)

d['name'] = 'Gumby'
d.setdefault('name', 'N/A')
print(d)

# 14、update 使用一个字典的项来更新另一个字典
print('14: ')
d = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2016'
}

x = {'title': 'Python Language Website'}
d.update(x)
print(d)
