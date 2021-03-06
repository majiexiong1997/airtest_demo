import logging

from airtest.core.android.adb import ADB
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from airtest.report.report import simple_report
from main_page.yaml_setting import yaml_load

class PdjsMainPage:
    main_package = "shangyoo.noahmobile.com"
    main_phone = "Android:///"
    package_path = r'C:\Users\majiexiong\Desktop\shangyoo.noahmobile.com_15.2.291.apk'

    def __init__(self):
        '''初始化设备'''
        self.device = connect_device(self.main_phone)
        auto_setup(__file__, logdir=False, devices=self.main_phone)
        self.poco = UnityPoco()
        self.setting()
        self.start_app()

    # def authorization(self):
    #     '''第一次授权'''
    #     f = yaml_load.yaml_load(r'../quanxian.yml')
    #     f = list(set(f['quanxian']))
    #     for i in f:
    #         print('adb shell pm grant {} {}'.format(self.main_package,i))
    #         os.popen('adb shell pm grant {} {}'.format(self.main_package,i))

    def check_app(self):
        '''检查app'''
        list_app = self.device.list_app()
        if self.main_package not in list_app:
            print('安装包体中')
            self.device.install_app(self.package_path, self.main_package)

            start_app(self.main_package)
            time.sleep(10)
            self.poco = UnityPoco()
        else:
            print('包体已安装')
            start_app(self.main_package)
            time.sleep(10)
            self.poco = UnityPoco()

    def setting(self):
        '''全局设置'''
        ST.FIND_TIMEOUT = 30  # 隐式等待
        ST.SNAPSHOT_QUALITY = 70  # 图片精度

    def report(self):
        '''报告生成'''
        simple_report(__file__, logpath=r'C:\Users\majiexiong\PycharmProjects\airtest_demo\center\log',
                      output=r'C:\Users\majiexiong\PycharmProjects\airtest_demo\center\log\log.html')

    def find(self, *element):
        '''基本方法查找'''
        if len(element) == 1:
            self.poco("{}".format(element[0])).wait_for_appearance()
            return self.poco("{}".format(element[0]))
        elif len(element) == 2:
            self.poco("{}".format(element[0])).child("{}".format(element[1])).wait_for_appearance()
            return self.poco("{}".format(element[0])).child("{}".format(element[1]))
        elif len(element) == 3:
            self.poco("{}".format(element[0])).child("{}".format(element[1])).child(
                "{}".format(element[2])).wait_for_appearance()
            return self.poco("{}".format(element[0])).child("{}".format(element[1])).child("{}".format(element[2]))

    def find_click(self, *element):
        '''基本点击'''
        return self.find(*element).click()

    def find_long_click(self, *element):
        '''基本长点击'''
        return self.find(*element).long_click()

    def find_chirden(self, *element):
        '''基本查找子节点所有子节点'''
        return self.find(*element).children()

    def find_text(self, *element):
        '''查找当前ui下文字'''
        return self.find(*element).get_text()

    def up_swipe(self):
        '''上滑'''
        self.width, self.height = self.device.get_current_resolution()
        start_pt = (self.width * 0.7, self.height * 0.7)
        end_pt = (self.width * 0.7, self.height * 0.3)
        swipe(start_pt, end_pt)

    def down_swipe(self):
        '''下滑'''
        self.width, self.height = self.device.get_current_resolution()
        start_pt = (self.width * 0.7, self.height * 0.3)
        end_pt = (self.width * 0.7, self.height * 0.7)
        swipe(start_pt, end_pt)

    def left_swipe(self):
        '''左滑'''
        self.width, self.height = self.device.get_current_resolution()
        start_pt = (self.width * 0.3, self.height / 2)
        end_pt = (self.width * 0.7, self.height / 2)
        swipe(start_pt, end_pt)

    def right_swipe(self):
        '''右滑'''
        self.width, self.height = self.device.get_current_resolution()
        start_pt = (self.width * 0.7, self.height / 2)
        end_pt = (self.width * 0.3, self.height / 2)
        swipe(start_pt, end_pt)

    def click_center(self):
        '''点击屏幕中央'''
        self.width, self.height = self.device.get_current_resolution()

        self.poco.click([0.1, 0.5])

    def start_app(self):
        '''
        启动app
        :return:
        '''
        start_app(self.main_package)

    def stop_app(self):
        '''停止app'''
        stop_app(self.main_package)

    def assert_type(self, testname, authname, testtitle):
        '''判断字体是否存在'''
        try:
            assert_equal(testname, authname, testtitle)
        except AssertionError:
            print('文字判定不对,错误字体{}'.format(testname))

    def assert_not_view(self, locator, other_locator):
        '''判断不存在元素,并创造测试分支'''
        try:
            assert_not_exists(locator, '元素{},寻找不到，忽略此步骤'.format(locator))
        except:
            self.poco.click(other_locator)

    def assert_view(self, locator):
        '''判断元素是否存在'''
        try:
            assert_exists(locator, '该元素{},寻找不到'.format(locator))
        except:
            print('没有找到元素{}'.format(locator))

    def screeen_size(self):
        '''获取当前屏幕尺寸'''
        self.width, self.height = self.device.get_current_resolution()
        return self.width, self.height


if __name__ == '__main__':
    PdjsMainPage()
