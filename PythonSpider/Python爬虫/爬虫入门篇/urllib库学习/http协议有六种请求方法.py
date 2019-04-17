'''
http协议有六种请求方法，get,head,put,delete,post,options，我们有时候需要用到PUT方式或者DELETE方式请求。

PUT：这个方法比较少见。HTML表单也不支持这个。本质上来讲， PUT和POST极为相似，都是向服务器发送数据，但它们之间有一个重要区别，PUT通常指定了资源的存放位置，而POST则没有，POST的数据存放位置由服务器自己决定。
DELETE：删除某一个资源。基本上这个也很少见，不过还是有一些地方比如amazon的S3云服务里面就用的这个方法来删除资源。

如果要使用 HTTP PUT 和 DELETE ，只能使用比较低层的 httplib 库。虽然如此，我们还是能通过下面的方式，使 urllib2 能够发出 PUT 或DELETE 的请求，不过用的次数的确是少，在这里提一下。

'''
import urllib.request as r
import urllib.parse as p
values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
values = p.urlencode(values).encode(encoding='utf-8')
print(values)
url='http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
request = r.Request(url=url, data=values)
#http的put请求方法
r.get_method = lambda: 'PUT' # or 'DELETE'
res = r.urlopen(request)
res = res.read()
print(res)
print(res.decode(encoding='utf-8'))

