'''
首先我们确定好页面的URL是 http://www.qiushibaike.com/hot/page/1，其中最后一个数字1代表页数，我们可以传入不同的值来获得某一页的段子内容。
我们初步构建如下的代码来打印页面代码内容试试看，先构造最基本的页面抓取方式，看看会不会成功

'''
# -*- coding:utf-8 -*-
import urllib.request as r
import urllib.parse as p

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
try:
    request = r.Request(url)
    response = r.urlopen(request)
    print(response.read())
except r.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)

#报错version, status, reason = self._read_status()
#应该是headers验证的问题，我们加上一个headers验证试试看吧