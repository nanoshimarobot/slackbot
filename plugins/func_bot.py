from selenium import webdriver
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import time

@respond_to('(.*),(.*),課題要求')
def search_task(message,something,something2):
    browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    browser.get('https://lms.anan-nct.ac.jp/ct/login')
    login_id = browser.find_element_by_name("userid")
    login_pass = browser.find_element_by_name("password")
    login_btn = browser.find_element_by_name("login")
    login_id.send_keys(something)
    time.sleep(1)
    login_pass.send_keys(something2)
    time.sleep(1)
    login_btn.click()
    time.sleep(1)
    name = browser.find_element_by_id("screenname")
    message.reply('貴様のお名前が分かりましたわ')
    message.reply('{0}'.format(name.text))
    browser.quit()

@respond_to('私は(.*)です')
@respond_to('わたしは(.*)です')
def hello(message,something):
    message.reply('まぁ！あなた{0}さんっていいますのね!!'.format(something))

@respond_to('(.*)')
def other(message, something):
    m = re.search('にゃーん',something)
    if m:
        message.reply('貴様のような高専生の分際で猫様の鳴き声を真似るか小僧')
    else:
        message.reply('わいはおぜうさま')
