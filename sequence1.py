# 写在字符串之前的话
# 数、字符等数据元素 >> 元组、列表、字符串等数据结构 >> 循环、选择语句 >> 模块
# 在我看来， 每一种编程语言对应的是其解决问题的思维。或者说，分解问题。
# so，一学基础；二悟思想。

# 字符串基本操作 2020/1/28

# 1、 字符串转义
print("let's go!")
print('let\'s go!')

# 2、字符串拼接
x = "hello, "
y = "world!"
print(x+y)

# 3、字符串表示 str 和 repr


'''months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# 月份的结尾设置
endings = ['st', 'nd', 'rd'] + 17*['th'] \
        + ['st', 'nd', 'rd'] + 7*['th'] \
        + ['st']
year = input('Year:')
month = input('month(1-12):')
day = input('day(1-31):')

month_number = int(month)
month_name = months[month_number - 1]

day_number = int(day)
day_end = endings[day_number-1]

# January 12th, 2020
print(month_name + ' ' + day + day_end + ', ' + year)
'''

# url = input('please enter the url:')
#
# # https://www.github.com
# domain = url[12:-4]
#
# print("Domain name :" + domain)



