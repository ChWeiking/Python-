#设置headers
'''
User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
 Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
 application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
 application/json ： 在 JSON RPC 调用时使用
 application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
 在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务
'''
import urllib.parse as p
import urllib.request as r
url = 'https://pan.baidu.com/disk/home?'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
referer='https://www.baidu.com/link?url=JzFKFWql03oLbutoFDy-59ySbrnAbdvw3WxM-HwYIL3&wd=&eqid=8c2b8b6000013c29000000065c716193'
values = {'username': '浅色咖啡厅', 'password': 'QM407342012'}
#agent就是请求的身份，如果没有写入请求身份，那么服务器不一定会响应，所以可以在headers中设置agent
#对付防盗链，服务器会识别headers中的referer是不是它自己，如果不是，有的服务器不会响应，所以我们还可以在headers中加入referer

headers = { 'User-Agent' : user_agent ,\
            'Referer':referer }
data = p.urlencode(values).encode(encoding='utf-8')
req = r.Request(url=url, data=data, headers=headers)
res = r.urlopen(req)
res = res.read()
print(res)
print(res.decode(encoding='utf-8'))

