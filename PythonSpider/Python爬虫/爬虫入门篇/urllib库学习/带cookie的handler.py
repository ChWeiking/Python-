import urllib.request as r
url = 'https://pan.baidu.com'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
cookie='PANPSC=8033687997400623097%3AYT8%2BiEEajGl1SDSAOlMu7%2Bn90oj%2BY%2FIsn4fsxlRvB9gVFfA13yIYHi5ph3pMHI18RF8aC5OnGNHxTJ3v1z1m%2BnsBaaQy1V9tSL2qB%2FM01waZAz9vS8ItkMH5sFiIFMHtLPY%2BF1C2z9dVUS71k5JenLUi%2F5S1zblt%2B%2Bo8ht7g5D2LIWeznIUCtSkA0KYPulwlfkiVl%2Ff%2FRfx4kU4b9dv9by76Oxw8WnAw; expires=Wed, 27-Feb-2019 13:44:03 GMT; path=/; domain=pan.baidu.com; httponly'
#agent就是请求的身份，如果没有写入请求身份，那么服务器不一定会响应，所以可以在headers中设置agent
#对付防盗链，服务器会识别headers中的referer是不是它自己，如果不是，有的服务器不会响应，所以我们还可以在headers中加入referer

headers = { 'User-Agent' : user_agent ,
            'cookie':cookie }
req = r.Request(url=url, headers=headers)
res = r.urlopen(req)
res = res.read()
print(res)
print(res.decode(encoding='utf-8'))