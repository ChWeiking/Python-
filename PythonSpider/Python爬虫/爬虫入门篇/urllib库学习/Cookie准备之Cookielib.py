'''
http.cookiejar模块的主要作用是提供可存储cookie的对象，以便于与urllib模块配合使用来访问Internet资源。Cookielib模块非常强大，
我们可以利用本模块的CookieJar类的对象来捕获cookie并在后续连接请求时重新发送，
比如可以实现模拟登录功能。该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。

它们的关系：CookieJar —-派生—->FileCookieJar  —-派生—–>MozillaCookieJar和LWPCookieJar

'''