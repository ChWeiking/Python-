'''
一般我们使用python的第三方库requests及框架scrapy来爬取网上的资源，但是设计javascript渲染的页面却不能抓取，
此时，我们使用web自动化测试化工具Selenium+无界面浏览器PhantomJS来抓取javascript渲染的页面，下面实现一个简单的爬取

https://www.cnblogs.com/chenice/p/6994111.html

'''

import xlsxwriter
from selenium import webdriver
from bs4 import BeautifulSoup

'''
https://www.cnblogs.com/buzhizhitong/p/5697526.html
'''

def get_grade(url):
    print(url)
    # 匿名爬虫
    # 假定9999端口开启tor服务
    service_args = ['--proxy=localhost:9999', '--proxy-type=socks5', ]
    driver = webdriver.PhantomJS(executable_path=r"F:\Techonolgoy\Python\file\spider\spider_tools\JS\1\phantomjs.exe")
    driver.get(url)
    data = driver.page_source
    # print(data)

    soup = BeautifulSoup(data, 'lxml')
    grades = soup.find_all('tr')
    for grade in grades:
        global i
        if '<td>' in str(grade):
            i += 1
            print(i)
            grade_text = grade.get_text()
            print(grade_text)
            grade_text = str(grade_text)
            city = grade_text[:-13]
            worksheet.write(i, 0, city)
            time = grade_text[-13:-9]
            worksheet.write(i, 1, time)
            subs = grade_text[-9:-7]
            worksheet.write(i, 2, subs)
            s = grade_text[-7:-3]
            worksheet.write(i, 3, s)
            grade = grade_text[-3:]
            worksheet.write(i, 4, grade)


i = -1
workbook = xlsxwriter.Workbook('grades.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 10)
worksheet.set_column('B:B', 10)
worksheet.set_column('C:C', 10)
worksheet.set_column('D:D', 10)
worksheet.set_column('E:E', 10)

urls = ['http://gkcx.eol.cn/soudaxue/queryProvince.html?page=' + str(num)
        for num in range(1, 166)]

for url in urls:
    get_grade(url)
workbook.close()