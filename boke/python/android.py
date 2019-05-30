# coding=utf-8
from appium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import keyword

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.1',
    'deviceName': '88MFBM72HGXZ',
    'udid': '88MFBM72HGXZ',
    'appPackage': 'com.izerocar.zycx',
    'appActivity': '.business.splash.SplashActivity',
    'appWaitActivity': '.business.home.HomeActivity',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
}
mm = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(3)

mm.find_element_by_id('com.izerocar.zycx:id/iv_close').click()
# 检查是否有活动页面弹窗，如果有就点击关闭
try:
    closePupop = mm.find_element_by_id('com.izerocar.zycx:id/iv_close')
except NoSuchElementException:
    pass
else:
    closePupop.click()
time.sleep(2)


def login_tset():
    Login = mm.find_element_by_id('com.izerocar.zycx:id/btn_portrait').click()
    Login = mm.find_element_by_id('com.izerocar.zycx:id/et_phone').send_keys('13804380438')
    Login = mm.find_element_by_id('com.izerocar.zycx:id/et_verification').send_keys('666666')
    Login = mm.find_element_by_id('com.izerocar.zycx:id/btn_login').click()


try:
    mm.find_element_by_id('com.izerocar.zycx:id/btn_confirm')
except NoSuchElementException:
    login_tset()
else:
    mm.find_element_by_id('com.izerocar.zycx:id/btn_confirm').click()
    quit()


