'''
我们已经做到把Cookie保存到文件中了，如果以后想使用，可以利用下面的方法来读取cookie并访问网站
设想，如果我们的 cookie.txt 文件中保存的是某个人登录百度的cookie，
那么我们提取出这个cookie文件内容，就可以用以上方法模拟这个人的账号登录百度
'''
import http.cookiejar as ck
import urllib.request as r

# 创建MozillaCookieJar实例对象
cookie = ck.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# 创建请求的request
req = r.Request("http://www.baidu.com")
# 利用urllib.request的build_opener方法创建一个opener
opener = r.build_opener(r.HTTPCookieProcessor(cookie))
response = opener.open(req)
res=response.read()
print(res.decode(encoding='utf-8'))

