import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def number_of_words():
    # 绘制图
    x_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
    y_data = [456, 283, 656, 380, 325, 204, 140, 177, 304, 37, 17, 156, 271, 98, 122, 78, 1, 183, 645, 254, 60, 105, 92,
              0, 6, 3]
    # plt.plot(x_data, y_data, color='red', linewidth=2.0,linestyle='-')
    plt.bar(x_data, y_data, fc='red')

    # 选择字体命名
    de_font = fm.FontProperties(fname='simfang.ttf')
    plt.title('背诵单词数量分布', fontproperties=de_font)

    # 标注数值
    for a, b in zip(x_data, y_data):
        plt.text(a, b, '%.0f' % b, verticalalignment='baseline', horizontalalignment='center')

    plt.xlabel('字母表', fontproperties=de_font)
    plt.ylabel('数量', fontproperties=de_font)

    # 保存画好的图(!先保存后显示)
    plt.savefig('./words.png')
    plt.show()


if __name__ == '__main__':
    number_of_words()
