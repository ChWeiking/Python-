'''
https://www.zhihu.com/question/34243513
'''
__author__ = 'CWQ'
# -*- coding:utf-8 -*-
import urllib.request as r
import re
import os
class Spider:
    def __init__(self):
        self.siteURL = 'https://www.zhihu.com/question/34243513'
    def getPage(self):
        try:
            # 构建请求的request
            request = r.Request(url=self.siteURL)
            # 利用urlopen获取页面代码
            response = r.urlopen(request)
            # 将页面转化为UTF-8编码
            res = response.read().decode('utf-8')
            #print(res)
            return res
        except r.URLError as e:
            if hasattr(e, "reason"):
                print("连接知乎失败,错误原因", e.reason)
                return None

    # 追加正则表达
    def getContents(self):
        res = self.getPage()
        pattern = re.compile('<noscript><img src="(.*?)" data-.*?</noscript>', re.S)
        items = re.findall(pattern, res)
        #for item in items:
        #   print(item)
        return items
    def write(self):
        path="D:\\MMpicture"
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)
        else:
            pass
        items=self.getContents()
        x=1
        for item in items:
            r.urlretrieve(item.strip(),path+'\%s.jpg' % x)
            x+=1
s=Spider()
#s.getPage()
#s.getContents()
s.write()