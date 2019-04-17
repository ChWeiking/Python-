import urllib.request as u
request = u.Request("https://accounts.douban.com/")
response = u.urlopen(request)
res=response.read()
print(res.decode(encoding='utf-8'))

