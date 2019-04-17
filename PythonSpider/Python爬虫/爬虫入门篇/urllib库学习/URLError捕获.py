'''
首先解释下URLError可能产生的原因：
1网络无连接，即本机无法上网
2连接不到特定的服务器
3服务器不存在

在代码中，我们需要用try-except语句来包围并捕获相应的异常。

'''
import urllib.request as r
req = r.Request('http://www.xx74xxx064798.com.cn')
try:
    r.urlopen(req)
except r.URLError as e:
    print(e.reason)

