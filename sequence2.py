# 序列之列表、元组基本操作
# 序列概览：
# 1）通用操作： 索引、切片、相加、相乘、成员资格检查 / 最大、最小、长度
# 2）区别是列表可以修改>> 列表方法
# 3）简单说明一下元组

# 1、索引
print('1:')
greetings = 'hello'
print(greetings[0])

# 2、实例
print('2:')
# months = [
#     'January',
#     'February',
#     'March',
#     'April',
#     'May',
#     'June',
#     'July',
#     'August',
#     'September',
#     'October',
#     'November',
#     'December'
# ]
#
# # 月份的结尾设置
# endings = ['st', 'nd', 'rd'] + 17*['th'] \
#         + ['st', 'nd', 'rd'] + 7*['th'] \
#         + ['st']
# year = input('Year:')
# month = input('month(1-12):')
# day = input('day(1-31):')
#
# month_number = int(month)
# month_name = months[month_number - 1]
#
# day_number = int(day)
# day_end = endings[day_number-1]
#
# # January 12th, 2020
# print(month_name + ' ' + day + day_end + ', ' + year)

# 3、切片及实例
# [a:b:c] a表示起始位置， b表示结束位置， c的大小表示步长，正负表示方向
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('3:')
print(numbers[::-2])
print(numbers[0:10:2])

# 4、序列相加和相乘
# 相加要是同一类型的
print('4:')
# # 方框内打印文字，下面代码英文可以 中文不太行
# sentences = input('Sentence: ')
#
# screen_width = 80
# text_width = len(sentences)
# print(text_width)
#
# box_width = text_width + 6
# left_margin = (screen_width - box_width) // 2
#
# print()
# print(' ' * left_margin + '+'   + '-'*(box_width-2) + '+')
# print(' ' * left_margin + '|  ' + ' '*text_width    + '  |')
# print(' ' * left_margin + '|  ' +    sentences      + '  |')
# print(' ' * left_margin + '|  ' + ' '*text_width    + '  |')
# print(' ' * left_margin + '+'   + '-'*(box_width-2) + '+')
# print()

# 5、成员资格：in， 返回的是布尔值 True False
print('5:')
permissions = 'rw'
print('w' in permissions)
print('x' in permissions)

# 6、长度 最小值、 最大值
print("6: ")
numbers = [100, 34, 678]
print(len(numbers))
print(max(numbers))
print(min(numbers))

# ---------列----------表------------
# 7、 函数list 转化为列表
print("7:")
x = list('hello')
print(x)

# 8.1、通过索引赋值修改列表
# 修改二字意味着可以增删插补
print("8.1:")
x = [1, 2, 1]
x[1] = 1
print(x)
# 8.2 通过切片赋值修改列表
# 当赋值为空时， 此时就起到了删除的作用
print('8.2:')
name = list('Perl')

name[2:] = 'ar'
print(name)

name[1:1] = 'ea'
print(name)

name[1:] = []  # 在这里提醒自己切片的规则是包含起点，而不包含终点
print(name)

# 9、删除列表指定元素
print('9:')
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2:4]
print(names)

# ------列--表--方--法-------
# object.method(arguments)

# 10、加一个对象 append
print('10:')
lst = [1, 2, 3]
lst.append(4)
print(lst)

# 11、clear
print('11: ')
lst.clear()
print(lst)

# 12、copy 常规赋值只是将一个名称关联到列表
print('12:')
a = [1, 2, 3]
b = a
b[1] = 4
print(a)

# >>
b = a.copy()
b[1] = 5
print(a)

# 13、count
print('13: ')
print(['to', 'be', 'or', 'not', 'to', 'be'].count('to'))

# 14、 extend 拓展列表，产生新的列表
print('14:')
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

# 15、index 返回指定值第一次出现的位置
print('15:')
knights = ['we', 'are', 'the', 'knights', 'who', 'say', 'ni']
print(knights.index('who'))
# 对于不在列表的，索引时会引发异常

# 16、insert 插入指定对象, 产生新的列表
print('16: ')
numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
print(numbers)

# 17、pop 删除一个元素 唯一即修改列表又返回非none值的方法
print('17:')
numbers.pop()
print(numbers)
# pop可以实现后进先出的栈（stack）

# 18、remove 删除列表中第一个为指定值的元素，无返回
print('18:')
x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('to')
print(x)

# 19、reverse 翻转列表，无返回
print('19:')
x.reverse()
print(x)

# 20、sort 使列表按顺序排列
print('20:')
x = [4, 6, 2, 1, 7, 9]
x.sort()
print(x)

# 如果想要保留原来的排序，可以这样做：(也可以用sort方法，然后copy)
x = [3, 2, 1]
y = sorted(x)
print(x)
print(y)

# sort的参数： key 排序标准； reverse 是否按相反顺序
x = ['aardvark', 'abalone', 'add', 'aerate']
x.sort(key=len, reverse=False)
print(x)

# ------元--组-------不可修改

# 21、创建方式： 逗号括起，圆括号
print('21:')
tu = (1, 2, 3)
print(tu)

# 创建一个值的元组，要加逗号
x = 42,
print(x)

# 22、函数tuple 转换序列为元组
print('22: ')
print(tuple([1, 2, 3]))


