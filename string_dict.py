# pi = 3.14
# print(pi)
#
# print("{0} {1:*>10.2f}".format("-", pi))
# ----------------------------------------------------------------------------------------
# 字典使用实例
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

# ------2020年1月19日 对字典实例的完善改进----------------

people = {
    'Alice': {'phone': '2341', 'addr': 'Foo drive 23', 'hobby': 'reading'},
    'Beth': {'phone': '9102', 'addr': 'Bar street 42', 'hobby': 'reading'},
    'Ceil': {'phone': '3158', 'addr': 'Baz avenue 90', 'hobby': 'reading'}
}

# 当一个键对应多个值时，应考虑描述性的标签
labels = {
    'phone': 'phone number',
    'addr': 'address',
    'hobby': 'hobby'
}

name = input('Name: ')

request = input('phone number(p) or address(a) or hobby(h): ')

# 如果做数据库，这里还需要考虑用户输入错的key怎么办 然后如何引导正确输入
if request == 'p':
    key = 'phone'
    label = labels.get(key)
    result = people.get(name, 'not available')
    print("{}'s {} is {}.".format(name, label, result[key]))

elif request == 'a':
    key = 'addr'
    label = labels.get(key)
    result = people.get(name, 'not available')
    print("{}'s {} is {}.".format(name, label, result[key]))

elif request == 'h':
    key = 'hobby'
    label = labels.get(key)
    result = people.get(name, 'not available')
    print("{}'s {} is {}.".format(name, label, result[key]))

else:
    print('数据查询项不存在')

