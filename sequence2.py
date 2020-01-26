# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# x = numbers[:11:2]
# print(x)

# ---------------------------------------------------------
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

# 改进 以句子为中心创建一个none的空白画板 画框

sentence = input(': ')

lg = len(sentence)

blank1 = [None] * (lg + 6)
blank2 = [None] * (lg + 6)
blank3 = [None] * (lg + 6)
blank4 = [None] * (lg + 6)
blank5 = [None] * (lg + 6)

print()
print(blank1)
print(blank2)
print(blank3)
print(blank4)
print(blank5)
print()
