# coding:utf-8

"""
Made by @Jessy 2020/03/28
"""


import sys
import os
import time
import config
from config import stuIDs, pwds
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

logText = ""


def printLog(msg):
    global logText
    print(msg)
    logText = logText + msg + '\n'


class Logger(object):

    def __init__(self, stream=sys.stdout):
        output_dir = "log"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        log_name = '{}.log'.format(time.strftime('%Y-%m-%d %H-%M'))
        filename = os.path.join(output_dir, log_name)

        self.terminal = stream
        self.log = open(filename, 'a+')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

def run():
    option = webdriver.ChromeOptions()
    # 用浏览器打开打卡的网址
    browser = webdriver.Chrome(options=option)
    target='http://tjxx.lnu.edu.cn/inputExt.asp'
    browser.get(target)

    # 输用户名和密码
    stuID_input = browser.find_element_by_name("userid")
    stuID_input.send_keys(stuID)

    user_pwd_input = browser.find_element_by_name("userpwd")
    user_pwd_input.send_keys(pwd)

    # 登陆
    login_button = browser.find_element_by_id("formSubmitBtn")
    ActionChains(browser).move_to_element(login_button).click(login_button).perform()
    printLog(stuIDs[i] + '登陆中')
    #print('登陆中')

    if browser.current_url == target:
        printLog('登陆失败')
        browser.quit()
    else:
        printLog('登陆成功')

    # 上次填报以来有无城市间流动经历？
    browser.find_element_by_xpath('//label[@class="weui-cell weui-check__label" and @for="r1"]').click()

    # 当日有无湖北（武汉）进出人员接触史？
    browser.find_element_by_xpath('//label[@class="weui-cell weui-check__label" and @for="r3"]').click()

    # 当日身体症状?
    browser.find_element_by_xpath('//label[@class="weui-cell weui-check__label" and @for="r8"]').click()

    # 当前是否隔离观察？
    browser.find_element_by_xpath('//label[@class="weui-cell weui-check__label" and @for="r10"]').click()

    # 是否在校在岗？
    browser.find_element_by_xpath('//label[@class="weui-cell weui-check__label" and @for="r5"]').click()

    # 提交
    browser.find_element_by_xpath('//*[@id="formSubmitBtn"]').click()

    #time.sleep(3)
    browser.implicitly_wait(10)
    # 确认提交
    browser.find_element_by_xpath('//div[@class="weui-dialog__ft"]/a[@class="weui-dialog__btn weui-dialog__btn_primary"]').click()

    #time.sleep(3)
    browser.implicitly_wait(2)
    # 关闭浏览器
    browser.quit()


if __name__ == '__main__':
    sys.stdout = Logger(sys.stdout)  # 将输出记录到log
    for i in range(0, len(stuIDs)):
        ifSuccess = False
        tryTimes = 0

        stuID = stuIDs[i]
        pwd = pwds[i]

        while (not ifSuccess) and tryTimes < 3:
            try:
                tryTimes += 1
                printLog('Trying ' + str(tryTimes) + ' times...')
                run()
                time.sleep(1)
                printLog(stuIDs[i] + '运行成功')
                ifSuccess = True
            except Exception as ex:
                #print('something wrong')
                printLog(stuIDs[i] + '运行失败')
                printLog('')
                time.sleep(3)

    printLog('See you next day~')