from airtest.core.api import *
import os
from poco.drivers.unity3d import UnityPoco

from airtest.core.android.android import Android




class MainPage:
    main_package = "shangyoo.noahmobile.com"
    main_phone = "Android:///"
    package_path = r'C:\Users\majiexiong\Desktop\shangyoo.noahmobile.com_15.2.291.apk'
    def __init__(self):

            self.device = connect_device(self.main_phone)
            auto_setup(__file__, logdir=False, devices=[self.main_phone])

            list_app = self.device.list_app()
            if self.main_package not in list_app:
                print('安装包体中')
                self.device.install_app(self.package_path,self.main_package)
                start_app(self.main_package)
                # time.sleep(10)
                self.poco = UnityPoco()
            else:
                print('包体已安装')
                start_app(self.main_package)
                time.sleep(10)
                self.poco = UnityPoco()
            ST.FIND_TIMEOUT = 30   # 隐式等待
            ST.SNAPSHOT_QUALITY = 70  #图片精度




    #基础查找
    def find(self,locator):
        return self.poco(locator)
    #查找当前UI下文字
    def find_text(self,locator):
        return self.poco(text=locator)
    #判断是否能找到当前UI并给出下一步操作
    def exites_find(self,locator):
        return self.poco(locator).exists()
    #等待元素出现
    def wait_start_find(self,locator):
        return self.poco(locator).wait_for_appearance()
    #等待元素消失
    def wait_end_find(self,locator):
        return self.poco(locator).wait_for_disappearance()
    #上滑  以当前屏幕显示效果分宽高，宽从左往右，高从上到下
    def up_swipe(self):
        self.width, self.height = self.device.get_current_resolution()
        start_pt = (self.width * 0.7, self.height * 0.7)
        end_pt = (self.width * 0.7, self.height * 0.3)
        swipe(start_pt, end_pt)
    #下滑
    def down_swipe(self):
        self.width, self.height = self.device.get_current_resolution()
        start_pt = (self.width * 0.7, self.height * 0.3)
        end_pt = (self.width * 0.7, self.height * 0.7)
        swipe(start_pt, end_pt)
    #左滑
    def left_swipe(self):
        self.width, self.height = self.device.get_current_resolution()
        start_pt = (self.width * 0.3, self.height/2)
        end_pt = (self.width * 0.7, self.height/2)
        swipe(start_pt, end_pt)
    #右滑
    def right_swipe(self):
        self.width, self.height = self.device.get_current_resolution()
        start_pt = (self.width * 0.7, self.height / 2)
        end_pt = (self.width * 0.3, self.height / 2)
        swipe(start_pt, end_pt)
    def up_swipe_by_skill(self):
        self.width, self.height = self.device.get_current_resolution()
        start_pt = (self.width * 0.3, self.height * 0.7)
        end_pt = (self.width * 0.3, self.height * 0.3)
        swipe(start_pt, end_pt)









if __name__ == '__main__':
    MainPage()