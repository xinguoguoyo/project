#coding=utf-8
from appium import webdriver
import time
import unittest
# import t1
#测试类继承自unittest.TestCase
class APPCenter(unittest.TestCase):
    def setUp(self):
        print "setUp now"
    def test1(self):
        print "test1 start"
        self.assertEqual(1,1,"test1 error")
    def test2(self):
        print "test2 start"
        self.assertEqual(1,2,"test2 error")
    def tearDown(self):
        print "tearDown "
if __name__ == '__main__':
    # unittest.main()
    testSuit=unittest.TestSuite()
    testLoader=unittest.defaultTestLoader
    test1=testLoader.loadTestsFromName("demo02.APPCenter.test1")
    test2=testLoader.loadTestsFromName("demo02.APPCenter.test2")
    test3 = testLoader.loadTestsFromName("demo02")
    testSuit.addTests([test1,test2,test3])
    unittest.TextTestRunner(verbosity=2).run(testSuit)

    # coding=utf-8
    from appium import webdriver
    import time
    import unittest


    # import t1
    # 测试类继承自unittest.TestCase
    class APPCenter(unittest.TestCase):
        def setUp(self):
            print "setUp now"

        def test1(self):
            print "test1 start"
            self.assertEqual(1, 1, "test1 error")

        def test2(self):
            print "test2 start"
            self.assertEqual(1, 2, "test2 error")

        def tearDown(self):
            print "tearDown "


    if __name__ == '__main__':
        # unittest.main()
        testSuit = unittest.TestSuite()
        testLoader = unittest.defaultTestLoader
        test1 = testLoader.loadTestsFromName("demo02.APPCenter.test1")
        test2 = testLoader.loadTestsFromName("demo02.APPCenter.test2")
        test3 = testLoader.loadTestsFromName("demo02")
        testSuit.addTests([test1, test2, test3])
        unittest.TextTestRunner(verbosity=2).run(testSuit)

        # coding=utf-8
        from appium import webdriver
        import time
        import unittest


        # 测试类继承自unittest.TestCase
        class APPCenter(unittest.TestCase):
            def setUp(self):
                desired_caps = {
                    # 指定测试APP的相关信息
                    'platformName': 'Android',
                    'platformVersion': '7.1.1',
                    # desired_caps['deviceName'] = '192.168.1.157'
                    # desired_caps['deviceName'] = 'vivo_X9i-60c9dcf1'
                    'deviceName': '60c9dcf1',
                    'appPackage': 'com.coomix.app.bus',
                    'appActivity': '.activity.WelcomeActivity',
                    'appWaitActivity': '.activity.MainActivity'

                }
                self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

            def test_sample(self):
                # e1=self.driver.find_element_by_id("com.coomix.app.bus:id/item_main_top_subway")
                e1 = self.driver.find_element_by_xpath("//android.widget.TextView[@text='地铁']")
                e1.click()
                time.sleep(3)

            def tearDown(self):
                self.driver.quit()


        if __name__ == '__main__':
            unittest.main()




