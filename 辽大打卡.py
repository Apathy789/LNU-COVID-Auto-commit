import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    #这里改成你的统一认证用户名和密码
    user_name = 'xxxx'
    pwd = 'xxxx'

    # 加上这两句话不打开浏览器
    option = webdriver.ChromeOptions()
    # option.add_argument('headless') # 设置option
    # 用浏览器打开打卡的网址
    browser = webdriver.Chrome(options=option)
    browser.get("http://tjxx.lnu.edu.cn/")

    # 输用户名和密码

    user_name_input = browser.find_element_by_name("userid")
    user_name_input.send_keys(user_name)

    user_pwd_input = browser.find_element_by_name("userpwd")
    user_pwd_input.send_keys(pwd)

    # 登陆
    login_button = browser.find_element_by_id("formSubmitBtn")
    ActionChains(browser).move_to_element(login_button).click(login_button).perform()
    print('登陆')

    # browser.get("http://tjxx.lnu.edu.cn/")

    # 上次填报以来有无城市间流动经历？

    browser.find_element_by_xpath( '//*[@id="sub_form"]/div[3]/div[2]/label[1]').click()

    # 当日有无湖北（武汉）进出人员接触史？
    browser.find_element_by_xpath('//*[@id="sub_form"]/div[4]/div[2]/label[1]').click()

    # 当日身体症状?
    browser.find_element_by_xpath( '//*[@id="sub_form"]/div[5]/div[2]/label[1]').click()

    # 当前是否隔离观察？
    browser.find_element_by_xpath( '//*[@id="sub_form"]/div[6]/div[2]/label[1]').click()

    # 是否在校在岗？
    browser.find_element_by_xpath( '//*[@id="sub_form"]/div[7]/div[2]/label[1]').click()

    # 提交
    browser.find_element_by_xpath('//*[@id="formSubmitBtn"]').click()

    time.sleep(5)
    # 确认提交
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/a[2]').click()

    time.sleep(5)
    # #关闭浏览器
    browser.quit()