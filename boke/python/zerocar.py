#coding=utf-8
from appium import webdriver
import time
import unittest
#class android(unittest.TestCase):
def app(self):
        desired_caps={
            #指定app相关信息
            'platformName':'Android',
            #名字
            'olatformVersion':'5.1',
            #版本
            'deviceName':'88MFBM72HGXZ',
            #设备名称
            'appPackage':'com.izerocar.zycx',
            #app包名
            'appActivity':'.business.splash.SplashActivity',
            #app活跃信息
            'appWaitActivity':'.business.home.HomeActivity',
            #
            'udid':'88MFBM72HGXZ',
            #
            'unicodeKeyboard':True,
        }
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        time.sleep(5)


def getSize(self):
        tanchuang = self.driver.find_element_by_class_name('android.widget.ImageView')
        x = self.driver.get_window_size(tanchuang, ['width'])
        y = self.driver.get_window_size(tanchuang, ['height'])
        return (x, y)

    # 获取控件的宽高
def swipeLeft(n, t):
            l = getSize()
            x1 = int(l[0] * 0.75)
            y1 = int(l[1] * 0.5)
            x2 = int(l[0] * 0.25)
            for i in range(0, n):
                time.sleep(3)
                self.driver.swipe(x1, y1, x2, y1, t)
        swipeLeft(4, 200)
# driver.find_element_by_class_name('android.widget.ImageView').click()#点击首页弹窗广告
# time.sleep(2)
# driver.find_element_by_id('com.izerocar.zycx:id/iv_back').click()#返回
# time.sleep(2)
# driver.find_element_by_id('com.izerocar.zycx:id/iv_close').click()#关闭首页弹窗
# time.sleep(2)
# driver.find_element_by_id('com.izerocar.zycx:id/tv_upgrade_cancel').click()#关闭更新提醒
# time.sleep(2)
# driver.find_element_by_id('com.izerocar.zycx:id/btn_use_car').click()#点击最近用车
# time.sleep(2)
# driver.find_element_by_id('com.izerocar.zycx:id/btn_location').click()#定位，回到当前位置
# time.sleep(2)
# driver.find_element_by_class_name('android.widget.ImageView').click()#点击选择城市
# time.sleep(2)
# driver.find_element_by_class_name('android.widget.TextView').click()#选中切换到惠州
# time.sleep(5)
# # search_text = driver.find_element_by_id('com.izerocar.zycx:id/et_search')
# # assert(search_text)
# # time.sleep(2)
# # search_text.click()
# # time.sleep(2)
# # text = '惠州体育馆'
# # search_text.send_keys(text.decode())
# e1=driver.find_element_by_id('com.izerocar.zycx:id/et_search')
# e1.send_keys(u'惠州体育馆')#搜索信息
# e1.clear()#清除信息
# driver.find_element_by_id('com.izerocar.zycx:id/btn_portrait').click()#点击个人信息，去登录页面
# driver.find_element_by_class_name('android.widget.EditText').send_keys('13838380438')#输入手机号
# driver.find_element_by_class_name('android.widget.EditText').send_keys('666666')#输入验证码
# driver.find_element_by_id('com.izerocar.zycx:id/btn_login').click()#点击登录
# time.sleep(5)
if __name__ == '__main__':
    unittest.main()