'''
以通过下面的方法把 Debug Log 打开，这样收发包的内容就会在屏幕上打印出来，方便调试，这个也不太常用，仅提一下
'''
import urllib.request as r
httpHandler = r.HTTPHandler(debuglevel=1)
httpsHandler = r.HTTPSHandler(debuglevel=1)
opener = r.build_opener(httpHandler, httpsHandler)
r.install_opener(opener)
response = r.urlopen('http://www.baidu.com')

