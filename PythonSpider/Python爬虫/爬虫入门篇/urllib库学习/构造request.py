import urllib.request as u
request = u.Request("https://accounts.douban.com/")  #构造Request
response = u.urlopen(request)
print(response.read())

