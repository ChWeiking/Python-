'''
https://www.zhihu.com/question/265637604/answer/355204424
'''
__author__ = 'CWQ'
# -*- coding:utf-8 -*-
import urllib.request as r
import re
import os
class Spider:
    def __init__(self):
        self.siteURL = 'https://www.zhihu.com/question/265637604'
        self.user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    def getPage(self):
        try:
            headers = {'User-Agent': self.user_agent}
            # 构建请求的request
            request = r.Request(url=self.siteURL,headers=headers)
            # 利用urlopen获取页面代码
            response = r.urlopen(request)
            # 将页面转化为UTF-8编码
            res = response.read().decode('utf-8')
            print(res)
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
s=Spider()
s.getPage()
#s.getContents()
