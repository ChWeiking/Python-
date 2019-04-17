'''
首先，我们先利用CookieJar对象实现获取cookie的功能，存储到变量中
'''
import urllib.request as r
import http.cookiejar as ck
#声明一个CookieJar对象实例来保存cookie
cookie = ck.CookieJar()
#利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器
handler=r.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = r.build_opener(handler)
#此处的open方法同urllib.request的urlopen方法
response = opener.open('http://www.baidu.com')
#将cookie保存到变量中，然后打印出了cookie中的值
for item in cookie:
    print('Name = '+item.name)
    print('Value = '+item.value)

