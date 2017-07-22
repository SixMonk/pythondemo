# BeautifulSoup Learning
# 官方文档：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
# 博客文档：http://cuiqingcai.com/1319.html

from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters;
and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# soup.prettify() 按照标准格式缩进输出
# print(soup.prettify())

# print(soup.title.string)
# >>> The Dormouse's story

# print(soup.p['class'])
# >>> ['title']

# print(soup.find_all('a'))
# print(soup.find(id="link3"))

# for link in soup.find_all('a'):
# 	print(link.get('href'))

# 获取所有的文字内容
# print(soup.get_text())

# soup 1.tag:标签 2.Name:标签的名称 3.Attributes : 属性

# 搜索文档树 find() & find_all()
# find_all(name,attrs,recursive,text,**kwargs)
# 按css 搜索
# print(soup.find_all('a', class_='sister'))

# 总结
# 1. 可以指定解析器 example >> soup = BeautifulSoup(html_doc, 'html.parser')
#    为html.parser解析器
# 2. 比较常用的是 find ,find_all() , get_text(), 传入正则 用法
# 3. example :
print(soup.find_all('li'))  # tag
print(soup.find('div', attrs={'class', 'hd'}))  # tag + attrs
print(soup.find('div', 'hd'))  # 同上 一样的效果
print(soup.find(text=re.compile('评价')))  # 匹配text = 评价
