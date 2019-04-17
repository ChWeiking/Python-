import urllib.request as u
response = u.urlopen("https://accounts.douban.com/")
print(response.read())

