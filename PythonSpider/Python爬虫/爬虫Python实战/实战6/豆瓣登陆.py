from selenium import webdriver
from time import sleep

def gethtml():
    loginurl = 'https://accounts.douban.com/passport/login?source=movie'  # 登录页面
    # browser = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    browser = webdriver.Chrome()
    browser.get(loginurl)  # 请求登录页面
    # data = browser.page_source
    # print(data)
    sleep(1)
    browser.find_element_by_xpath('//li[@class = "account-tab-account"]').click()
    sleep(1)
    # browser.find_element_by_id('username').clear()  # 获取用户名输入框，并先清空
    browser.find_element_by_id('username').send_keys("123456")  # 输入用户名
    # browser.find_element_by_id('password').clear()  # 获取密码框，并清空
    browser.find_element_by_id('password').send_keys("123456")  # 输入密码


    sleep(20)

gethtml()
