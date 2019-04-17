#get方式数据传送
import urllib.request as r
import urllib.parse as p
values = {"username": "15024196167", "password": "Qm40734201272!"}
data = p.urlencode(values)
#print(data)
url = "https://accounts.douban.com/passport/login?source=movie"
request = r.Request(url='%s%s%s' % (url,'?',data))
response = r.urlopen(request)
res=response.read()
print(res.decode(encoding='utf-8'))

'''
import urllib.request as r
import urllib.parse as p

values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
data = p.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = r.Request(geturl)
response = r.urlopen(request)
res=response.read()
#输出内容(python3默认获取到的是16进制'bytes'类型数据
# Unicode编码，如果如需可读输出则需decode解码成对应编码)
# :b'\xe7\x99\xbb\xe5\xbd\x95\xe6\x88\x90\xe5\x8a\x9f'
print(res.decode(encoding='utf-8'))

'''