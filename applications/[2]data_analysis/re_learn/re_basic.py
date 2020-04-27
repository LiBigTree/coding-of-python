# ^[A-Za-z]+$ 由26个字母组成的字符串
# ^[A-Za-z0-9]+$ 由26个字母和数字组成的字符串
# ^-?\d+$ 整数形式的字符串 ？表示前一个字符的0次或1次拓展 ^/$为开头结尾组合 +为重复1到无限次组合
# ^[0-9]*[1-9]*[0-9]*$ 正整数形式的字符串
# [1-9]\d{5} 中国境内邮政编码，6位     {5}表示拓展前一个字符5次
# [\u4e00-\u9fa5] 匹配中文字符,utf-8编码约定了中文字符的取值范围
# \d{3}-\d{8}|\d{4}-\d{7} 国内电话号码

# 匹配IP地址的正则表达式 四段的，0-255范围： \d+.\d+.\d+.\d+ 或者 \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}
# 精确表达：0-99 100-199 200-249 250-255分别表达
# !分析方法：逐个位数分析，找规律表达
# (([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5]).){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])
import re

# 原生字符串
# print(r'[1-9]\d{5}')

# re.search(pattern, string, flags=0) 在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
# pattern：正则表达式的字符串或原生字符串表示
# string：待匹配字符串
# flags： 正则表达式使用时的控制标记
# - 常用标记
# - re.I re.IGNORECASE 忽略正则表达式的大小写，[A-Z]能够匹配小写字符
# - re.M re.MULTILINE 正则表达中的^操作符能够将给定字符串的每行当作匹配开始
# - re.S re.DOTALL 正则表达式中的.操作符能够匹配所有字符，默认匹配除换行外的所有字符
match = re.search(r'[1-9]\d{5}', 'BIT 100081')
if match:
    print(type(match.group))
    print('搜索：', match.group(0))

# re.match(pattern, string, flags=0)
# 从一个字符串的开始位置起匹配正则表达式，返回match对象
match = re.match(r'[1-9]\d{5}', 'BIT 100081')
if match:
    print('匹配：', match.group(0))
# 没有匹配到，是空的

# # re.findall(pattern, string, flags=0) 返回列表
ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print('子串查找：', ls)

# re.split(pattern, string, maxsplit=0, flags=0)
# 把匹配内容作为分割的标准去分割字符串，返回列表
# # 最大分割数，剩余部分作为最后一个元素输出
# r = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084')
# print(r)
# r = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1)
# print('加入最大匹配：', r)
#
# # re.finditer(pattern, string, flags=0)
# # 返回可迭代对象
# for i, m in enumerate(re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084')):
#     if m:
#         print(i, m.group(0))
#
# # re.sub(pattern, repl, string, count=0, flags=0)
# # 返回字符串
# # repl 要替换的
# # count:最大匹配次数
# rp = re.sub(r'[1-9]\d{5}', ': zipcode', 'BIT100081 TSU100084')
# print(rp)
#
# # match对象
# match = re.search(r'[1-9]\d{5}', 'BIT 100081')
# if match:
#     print(type(match.group))
#     print(match.re)
#     print(match.span())
#     print(match.group(0))

# 贪婪匹配和最小匹配
match = re.search(r'PY.*N', 'PYANBNCNDN')
print('贪婪匹配：', match.group(0))

match = re.search(r'PY.*?N', 'PYANBNCNDN')
print('最小匹配：', match.group(0))
# 最小匹配需要拓展
