import urllib
from PIL import Image
from selenium import webdriver
import pandas as pd
import numpy as np
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def gethtml(url):
    #chrome_options = Options()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-gpu')
    #driver = webdriver.Chrome(executable_path='D:/chromedriver/chromedriver.exe', chrome_options=chrome_options)
    #driver.close()

    loginurl='https://accounts.douban.com/passport/login?source=movie'    # 登录页面
    browser = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    #browser.set_window_size(480, 800)  # set browser size.
    #browser = webdriver.Firefox()
    #browser = webdriver.Chrome()
    #browser = webdriver.Ie()
    browser.get(loginurl)    # 请求登录页面
    #data = browser.page_source
    #print(data)
    browser.find_element_by_xpath('//li[@class = "account-tab-account"]').click() #selenium只能对界面显示的元素进行操作
    browser.find_element_by_name('username').clear()  # 获取用户名输入框，并先清空
    browser.find_element_by_name('username').send_keys(u'15024196167') # 输入用户名
    browser.find_element_by_name('password').clear()  # 获取密码框，并清空
    browser.find_element_by_name('password').send_keys(u'Qm40734201272!') # 输入密码

    # 验证码手动处理,输入后，需要将图片关闭才能继续执行下一步
    #captcha_link = browser.find_element_by_id('code').get_attribute('src')
    #urllib.request.urlretrieve(captcha_link,'captcha.jpg')
    #Image.open('captcha.jpg').show()
    #captcha_code = input('Pls input captcha code:')
    #browser.find_element_by_id('code').send_keys(captcha_code)
    #browser.find_element_by_css_selector('input[class="account-form-input"]').click()
    browser.get(url)
    browser.implicitly_wait(10)
    return(browser)

def getComment(url):
    i = 1
    AllArticle = pd.DataFrame()
    browser = gethtml(url)
    while True:
        s = browser.find_elements_by_class_name('comment-item')
        articles = pd.DataFrame(s, columns=['web'])
        articles['user'] = articles.web.apply(lambda x: x.find_element_by_tag_name('a').get_attribute('title'))
        articles['comment'] = articles.web.apply(lambda x: x.find_element_by_class_name('short').text)
        articles['star'] = articles.web.apply(lambda x: x.find_element_by_xpath("//span[@class='comment-info']/span[2]").get_attribute('title'))
        articles['date'] = articles.web.apply(lambda x: x.find_element_by_class_name('comment-time').get_attribute('title'))
        articles['vote'] = articles.web.apply(lambda x: np.int(x.find_element_by_class_name('votes').text))
        del articles['web']
        AllArticle = pd.concat([AllArticle, articles], axis=0)
        print('第' + str(i) + '页完成!')
        try:
            if i == 1:
                browser.find_element_by_xpath("//*[@id='paginator']/a").click()
            else:
                browser.find_element_by_xpath("//*[@id='paginator']/a[3]").click()
            browser.implicitly_wait(10)
            time.sleep(3)  # 暂停3秒
            i = i + 1
        except:
            AllArticle = AllArticle.reset_index(drop=True)
            return AllArticle
    AllArticle = AllArticle.reset_index(drop=True)
    return AllArticle
url = 'https://movie.douban.com/subject/26636712/comments?status=P'
result = getComment(url)
result.to_excel('t.xlsx', encoding='utf-8', index=False, header=False)
