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

url = input('please enter the url:')

# https://www.github.com
domain = url[12:-4]

print("Domain name :" + domain)





