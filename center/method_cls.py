from airtest.core.api import *

from center.main_page import MainPage
import re
import yaml
class method_cls(MainPage):


    def find(self,*element):
        '''基本方法查找'''
        if len(element) == 1:
            self.poco("{}".format(element[0])).wait_for_appearance()
            return self.poco("{}".format(element[0]))
        elif len(element) == 2:
            self.poco("{}".format(element[0])).child("{}".format(element[1])).wait_for_appearance()
            return self.poco("{}".format(element[0])).child("{}".format(element[1]))
        elif len(element) == 3:
            self.poco("{}".format(element[0])).child("{}".format(element[1])).child("{}".format(element[2])).wait_for_appearance()
            return self.poco("{}".format(element[0])).child("{}".format(element[1])).child("{}".format(element[2]))

    def find_click(self,*element):
        '''基本点击'''
        self.find(*element).click()

    def find_long_click(self,*element):
        '''基本长点击'''
        self.find(*element).long_click()

    def find_chirden(self,*element):
        '''基本查找子节点所有孩子'''
        self.find(*element).children()
    def find_text(self, locator):
        '''查找当前ui下文字'''
        return self.poco(text=locator)

    # 上滑  以当前屏幕显示效果分宽高，宽从左往右，高从上到下
    def up_swipe(self):
        self.width, self.height = self.device.get_current_resolution()
        start_pt = (self.width * 0.7, self.height * 0.7)
        end_pt = (self.width * 0.7, self.height * 0.3)
        swipe(start_pt, end_pt)
    def up_swipe_for_rank(self):
        self.width, self.height = self.device.get_current_resolution()
        start_pt = (self.width * 0.3, self.height * 0.7)
        end_pt = (self.width * 0.3, self.height * 0.3)
        swipe(start_pt, end_pt)


    # 下滑         可根据实际游戏情况修改
    def down_swipe(self):
        self.width, self.height = self.device.get_current_resolution()
        start_pt = (self.width * 0.7, self.height * 0.3)
        end_pt = (self.width * 0.7, self.height * 0.7)
        swipe(start_pt, end_pt)


    # 左滑         可根据实际游戏情况修改
    def left_swipe(self):
        self.width, self.height = self.device.get_current_resolution()
        start_pt = (self.width * 0.3, self.height / 2)
        end_pt = (self.width * 0.7, self.height / 2)
        swipe(start_pt, end_pt)
    def left_swipe_for_rank(self):
        self.width, self.height = self.device.get_current_resolution()
        start_pt = (self.width * 0.3, self.height * 0.15)
        end_pt = (self.width * 0.7, self.height / 0.15)
        swipe(start_pt, end_pt)


    # 右滑         可根据实际游戏情况修改
    def right_swipe(self):
        self.width, self.height = self.device.get_current_resolution()
        start_pt = (self.width * 0.7, self.height / 2)
        end_pt = (self.width * 0.3, self.height / 2)
        swipe(start_pt, end_pt)


    # 技能上滑
    def up_swipe_by_skill(self):
        self.width, self.height = self.device.get_current_resolution()
        start_pt = (self.width * 0.3, self.height * 0.7)
        end_pt = (self.width * 0.3, self.height * 0.3)
        swipe(start_pt, end_pt)


    # 点击屏幕中央  可根据实际游戏情况修改
    def click_center(self):
        self.width, self.height = self.device.get_current_resolution()

        self.poco.click([0.1, 0.5])
    # 停止app
    def stop_app(self):
        stop_app(self.main_package)

    #判断字体是否存在
    def assert_type(self, testname, authname, testtitle):
        try:
            assert_equal(testname, authname, testtitle)
        except AssertionError:
            print('文字判定不对,错误字体{}'.format(testname))
    #判断不存在元素,并创造测试分支
    def assert_not_view(self,locator,other_locator):
        try:
            assert_not_exists(locator,'元素{},寻找不到，忽略此步骤'.format(locator))
        except :
            self.poco.click(other_locator)
    #判断元素是否存在
    def assert_view(self,locator):
        try:
            assert_exists(locator,'该元素{},寻找不到'.format(locator))
        except:
            print('没有找到元素{}'.format(locator))
    def screeen_size(self):
        self.width,self.height = self.device.get_current_resolution()
        return self.width,self.height




