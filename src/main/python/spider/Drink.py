# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Drink.py
# @description Drink
# @author WcJun
# @date 2020/07/11
# ---------------------------------------------

# ---------------------------------------------
"""
python -m pip --default-timeout=1000 install jieba -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
python -m pip --default-timeout=1000 install wordcloud -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
python -m pip --default-timeout=1000 install imageio -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
python -m pip --default-timeout=1000 install matplotlib -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
"""
# ---------------------------------------------


import random
import pylab as plt

import jieba
from wordcloud import WordCloud


# from imageio import imread


def main():
    result = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}
    words = []
    train_count = 10000001
    for i in range(1, train_count):
        # A 出拳: gesture_a  喊出 数值: shout_a
        gesture_a, shout_a = punch()
        # B 出拳: gesture_b  喊出 数值: shout_b
        gesture_b, shout_b = punch()
        print(f"-------------------------------------------- {i}")
        # print(f"A第{i}次出拳:{gesture_a},喊出数值:{shout_a} ")
        # print(f"B第{i}次出拳:{gesture_b},喊出数值:{shout_b} ")
        gesture_sum = gesture_a + gesture_b
        if gesture_sum == shout_a and gesture_sum != shout_b:
            # print(f"第{i}次划拳:A出拳:{gesture_a},:B出拳:{gesture_b},刚好和等于A的喊出的数值{shout_a} == A WIN")
            update_count(result, shout_a)
            words.append(str(f"{chinese_upper_convert(gesture_a)}{chinese_upper_convert(shout_a)}"))
        if gesture_sum == shout_b and gesture_sum != shout_a:
            # print(f"第{i}次划拳:B出拳:{gesture_b},:A出拳:{gesture_a},刚好和等于A的喊出的数值{shout_b} == B WIN")
            update_count(result, shout_b)
            words.append(str(f"{chinese_upper_convert(gesture_b)}{chinese_upper_convert(shout_b)}"))
        # if gesture_sum == shout_b and gesture_sum == shout_a:
        #     print(f"第{i}次划拳:A出拳:{gesture_b},:A出拳:{gesture_a},刚好和等于A|B的喊出的数值{shout_a} == 平局")

    if len(words) > 0:
        draw_word_cloud(words)
    x_data = list(range(11))
    y_data = list(result.values())
    plt.plot(x_data, y_data, color='blue', linewidth=1.0)
    plt.show()
    return


def punch() -> ():
    """
    划拳 \n
    第一个数值 表示: 划拳时出的手势
    第二个数值 表示: 划拳时喊出的数值
    :return:
    """
    # 划拳的手势 -> 自己出 的数值
    gesture = random.randint(0, 5)
    # 喊出的数值
    shout = random.randint(gesture, gesture + 5)

    # 此处 还没有考虑 - 臭拳 - 即:自爆的场景

    return gesture, shout


def update_count(result: dict, shout: int) -> None:
    """
    更新数量 \n
    :param result:
    :param shout:
    :return:
    """
    key = str(shout)
    count = result.get(key) + 1
    result[key] = count

    return


def word_cut(text: str, delimiter: str) -> str:
    """
    Jieba 分词 \n
    :param text: 分词文本
    :param delimiter: 分隔符
    :return: 分词结果 \n
    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
    """
    # 选择分词模式
    words = jieba.cut(text, cut_all=True)
    print(words)
    # 分词后在单独个体之间加上空格
    result = delimiter.join(words)

    # 返回分词结果
    return result


def draw_word_cloud(words: list) -> None:
    """
    将分词的结果最绘制成词云
    :param words: 分词结果
    :return: None
    """
    FONT = "msyh.ttc"
    splitter = " "
    words_str = splitter.join(words)

    # 读取背景图片
    # background = imread('background.png')

    word_cloud = WordCloud(
        # mask=background,
        width=900,
        height=600,
        background_color='white',
        font_path=FONT
    )
    word_cloud.generate(words_str)
    word_cloud.to_file("drink.png")

    return


num_dict = {
    '0': '零',
    '1': '壹', '2': '贰', '3': '叁', '4': '肆', '5': '伍',
    '6': '陆', '7': '柒', '8': '捌', '9': '玖', '10': '拾'
}


def chinese_upper_convert(key: int) -> str:
    """
    将阿拉伯数值抓换为中文大写
    :param key:
    :return:
    """
    return num_dict.get(str(key))
