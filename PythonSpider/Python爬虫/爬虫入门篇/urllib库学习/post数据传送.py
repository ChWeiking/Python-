#post数据传送
import urllib.parse as p
import urllib.request as r
values = {}
values['username'] = "15024196167"
values['password'] = "Qm40734201272!"
values = p.urlencode(values).encode(encoding='utf-8')
#print(values)
url='https://accounts.douban.com/passport/login?source=movie'
request = r.Request(url=url,data=values)
response = r.urlopen(request)
res = response.read()
print(res.decode(encoding='utf-8'))
