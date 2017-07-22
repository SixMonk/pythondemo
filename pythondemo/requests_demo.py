# -*- coding: utf-8 -*-

# python http请求 >>> requests
# 文档：http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
import requests

# 一览
# r = requests.get('http://github.com/timeline.json')
# print(r.text)


# 1. url 传递参数
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("http://httpbin.org/get", params=payload)
# print(r.url)
# print(r.text)

# 2. 二进制响应内容
# r = requests.get(
#    "http://photo.weibo.com/1697371637/wbphotos/large/mid/4132400554488746/pid/652bd5f5ly1fhswr9j7wmj20ku0kugok")
# print(r.content)
# print('ok')

# 3. json 内容响应
# r.json 失败 >>> 401
# r = requests.get('http://github.com/timeline.json')
# print(r.json())

# 4. headers
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 \
#        (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
# data = requests.get("http://movie.douban.com/top250/", headers=headers).content
# print(data)

# 5. Form形式请求 >>> html表单
# payload = {'key1': 'value1', 'key2':'value2'}
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)

# 6. json格式请求
# payload = {'some': 'data'}
# r = requests.post("https://api.github.com/some/endpoint", json=payload)
# print(r.text)

# 7. 响应状态码
# r = requests.get('http://httpbin.org/get')
# print(r.status_code)

# 8. 超时机制
# r = requests.get('http://github.com', timeout=0.1)
