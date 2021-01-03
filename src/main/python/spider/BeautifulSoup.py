# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file BeautifulSoup.py
# @description BeautifulSoup
# @author WcJun
# @date 2020/07/05
# ---------------------------------------------


from bs4 import BeautifulSoup
from bs4.element import Comment

html = """
<title id = 'title'>尚学堂</title>
<div class='info' float='left'>Welcome to SXT</div>
<div class='info' float='right'>
    <span>Good Good Study</span>
    <a href='www.bjsxt.cn'></a>
    <strong><!--没用--></strong>
</div>
"""


def main():
    soup = BeautifulSoup(html, 'html.parser')

    print("--------------------tag--------------------------")
    # <title>尚学堂</title>
    print(soup.title)
    # <div class="info" float="left">Welcome to SXT</div>
    print(soup.div)
    # {'class': ['info'], 'float': 'left'}
    print(soup.div.attrs)
    # <class 'dict'>
    print(type(soup.div.attrs))
    # ['info']
    print(soup.div.get('class'))
    # left
    print(soup.div['float'])
    # www.bjsxt.cn
    print(soup.a['href'])

    print("--------------------content--------------------------")
    # Welcome to SXT
    print(soup.div.string)
    # <class 'bs4.element.NavigableString'>
    print(type(soup.div.string))
    # Welcome to SXT
    print(soup.div.text)
    print("--------------------comment--------------------------")
    # <class 'bs4.element.Tag'>
    print(type(soup.strong))
    # <class 'bs4.element.Comment'>
    print(type(soup.strong.string))
    # 没用
    print(soup.strong.string)

    if type(soup.strong.string) == Comment:
        print("--------------------if--------------------------")
        print(soup.strong.string)
        print("--------------------if-prettify()--------------------------")
        print(soup.strong.prettify())
    else:
        print("--------------------if-else--------------------------")
        print(soup.strong.text)

    print("--------------------findall()--------------------------")
    print(soup.find_all('title'))
    # 通过 id 选择器
    print(soup.find_all(id='title'))
    print(soup.find_all(class_='info'))
    # [<div class="info" float="left">Welcome to SXT</div>]
    print(soup.find_all(attrs={'float': 'left'}))
    # [<div class="info" float="left">Welcome to SXT</div>]
    print(soup.find_all("div", attrs={'float': 'left'}))

    print("--------------------css()--------------------------")
    print(soup.select('title'))
    # 尚学堂
    print(soup.select('title')[0].text)
    print(soup.select('#title'))
    print(soup.select('.info'))
    print("--------------------css-selector()--------------------------")
    # [<span>Good Good Study</span>]
    print(soup.select('div span'))
    # [<span>Good Good Study</span>]
    print(soup.select('div > span'))
    # [<span>Good Good Study</span>]
    print(soup.select('div')[1].select('span'))
    # [<a href="www.bjsxt.cn"></a>]
    print(soup.select('div')[1].select('a'))
