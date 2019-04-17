'''
审查元素，我们可以看到百度贴吧每一层楼的主要内容

'''
__author__ = 'CWQ'
# -*- coding:utf-8 -*-
import urllib.request as r
import re
# 百度贴吧爬虫类
class BDTB:
    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self, baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)

    # 传入页码，获取该页帖子的代码
    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = r.Request(url)
            response = r.urlopen(request)
            #print(response.read().decode('utf-8'))
            return response
        except r.URLError as  e:
            if hasattr(e, "reason"):
                print("连接百度贴吧失败,错误原因", e.reason)
                return None

    # 获取帖子标题
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<title>(.*?)</title>', re.S)
        result = re.search(pattern, page.read().decode('utf-8'))
        if result:
            #print(result.group(1)) #测试输出
            return result.group(1).strip()
        else:
            return None

    # 获取帖子一共有多少页
    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page.read().decode('utf-8'))
        if result:
            print(result.group(1))  #测试输出
            return result.group(1).strip()
        else:
            return None

    # 获取每一层楼的内容,传入页面内容
    def getContent(self, page):
        pattern = re.compile('width=.*?height=.*?<br>(.*?)</cc>', re.S)
        items = re.findall(pattern, page.read().decode('utf-8'))
        for item in items:
            print(item)


baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL, 1)
page = bdtb.getPage(1)
bdtb.getContent(page)