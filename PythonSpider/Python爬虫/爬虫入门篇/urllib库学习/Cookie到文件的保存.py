'''
将ookie保存到文件使用FileCookieJar这个对象，在这里我们使用它的子类MozillaCookieJar来实现Cookie的保存
'''
import http.cookiejar as ck
import urllib.request as r

# 设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = ck.MozillaCookieJar(filename)
# 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器
handler = r.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = r.build_opener(handler)
# 创建一个请求，原理同urllib.request的urlopen
response = opener.open("http://www.baidu.com")
# 保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)
#ignore_discard的意思是即使cookies将被丢弃也将它保存下来，ignore_expires的意思是如果在该文件中cookies已经存在，
# 则覆盖原文件写入，在这里，我们将这两个全部设置为True。运行之后，cookies将被保存到cookie.txt文件中
