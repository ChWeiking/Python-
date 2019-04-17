'''
提取某一页的所有段子
获取了HTML代码之后，我们开始分析怎样获取某一页的所有段子。

首先我们审查元素看一下，按浏览器的F12

我们可以看到，每一个段子都是<div class=”article block untagged mb15″ id=”…”>…</div>包裹的内容。

现在我们想获取发布人，发布日期，段子内容，以及点赞的个数。不过另外注意的是，段子有些是带图片的，如果我们想在控制台显示图片是不现实的，所以我们直接把带有图片的段子给它剔除掉，只保存仅含文本的段子。

所以我们加入如下正则表达式来匹配一下，用到的方法是 re.findall 是找寻所有匹配的内容。方法的用法详情可以看前面说的正则表达式的介绍。

好，我们的正则表达式匹配语句书写如下，在原来的基础上追加如下代码


'''
import urllib.request as r
import urllib.parse as p
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
headers = { 'User-Agent' : user_agent }
try:
    request = r.Request(url=url,headers = headers)
    response = r.urlopen(request)
    res=response.read()
#    print(res.decode(encoding='utf-8'))
except r.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)
#运行终于正常了，打印出了第一页的HTML代码
#追加正则表达
content = res.decode('utf-8')
pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<span>(.*?)'+
                         '</span>.*?<div class="stats.*?class="number">(.*?)</i>',re.S)
items = re.findall(pattern,content)
for item in items:
    print(item[0],item[1],item[2])

#1）.*? 是一个固定的搭配，.和*代表可以匹配任意无限多个字符，加上？表示使用非贪婪模式进行匹配，也就是我们会尽可能短地做匹配，以后我们还会大量用到 .*? 的搭配。

#2）(.*?)代表一个分组，在这个正则表达式中我们匹配了三个分组，在后面的遍历item中，item[0]就代表第一个(.*?)所指代的内容，item[1]就代表第二个(.*?)所指代的内容，以此类推。

#3）re.S 标志代表在匹配时为点任意匹配模式，点 . 也可以代表换行符。

#这样我们就获取了发布人，发布内容，以及点赞数。
#带图片的段子进行过滤
#for item in items:
#        haveImg = re.search("img",item[3])
#        if not haveImg:
#            print item[0],item[1],item[2],item[4]



