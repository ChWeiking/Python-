'''
#报错version, status, reason = self._read_status()
#应该是headers验证的问题，我们加上一个headers验证试试看吧
'''
# -*- coding:utf-8 -*-
import urllib.request as r
import urllib.parse as p

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
headers = { 'User-Agent' : user_agent }
try:
    request = r.Request(url=url,headers = headers)
    response = r.urlopen(request)
    res=response.read()
    print(res.decode(encoding='utf-8'))
except r.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)
#运行终于正常了，打印出了第一页的HTML代码