'''
urlopen方法，第三个参数就是timeout的设置，可以设置等待多久超时，为了解决一些网站实在响应过慢而造成的影响。
'''
import urllib.request as r
response = r.urlopen('http://www.baidu.com', timeout=10)


