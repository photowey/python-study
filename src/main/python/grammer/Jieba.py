# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Jieba.py
# @description 
# @author WcJun
# @date 2020/06/21
# ---------------------------------------------

import jieba
from wordcloud import WordCloud


def word_cut(text: str, delimiter: str) -> str:
    """
    Jieba 分词

    :param text: 分词文本
    :param delimiter: 分隔符
    :return: 分词结果

    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
    """
    # 选择分词模式
    words = jieba.cut(text, cut_all=True)
    print(words)
    # 分词后在单独个体之间加上空格
    result = delimiter.join(words)

    # 返回分词结果
    return result


word = "床前明月光，疑是地上霜。举头望明月，低头思故乡。"
splitter = " "
word_list = word_cut(word, splitter)

FONT = "msyh.ttc"

word_cloud = WordCloud(
    background_color='white',
    font_path=FONT
).generate(word_list)
word_cloud.to_file("word_cloud.png")
