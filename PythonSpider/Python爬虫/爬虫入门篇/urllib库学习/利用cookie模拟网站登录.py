'''
利用cookie实现模拟登录，并将cookie信息保存到文本文件中
在Python3中，将中文进行编码使用函数
urllib.parse.quote(string, safe='/', encoding=None, errors=None)
而将编码后的字符串转为中文，则使用
urllib.parse.unquote(string, encoding='utf-8', errors='replace')

'''
import urllib.parse as p
import urllib.request as r
import http.cookiejar as ck
filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = ck.MozillaCookieJar(filename)
opener = r.build_opener(r.HTTPCookieProcessor(cookie))
#中文进行编码,提交类型不能为str，需要为byte类型
postdata = p.urlencode({'username': '浅色咖啡厅','password': 'QM407342012'}).encode('utf-8')
# 登录百度网盘的URL
loginUrl = 'https://pan.baidu.com/'
# 模拟登录，并把cookie保存到变量
result = opener.open(loginUrl, postdata)
# 保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
# 利用cookie请求访问另一个网址
gradeUrl = 'https://pan.baidu.com/pcloud/home'
# 请求访问的另一个网址
result = opener.open(gradeUrl)
res=result.read()
print(res.decode(encoding='utf-8'))
