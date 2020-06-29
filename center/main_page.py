from airtest.core.api import *
import os
from poco.drivers.unity3d import UnityPoco

from airtest.core.android.android import Android




class MainPage:
    main_package = "shangyoo.noahmobile.com"
    main_phone = "Android:///"
    package_path = r'C:\Users\majiexiong\Desktop\shangyoo.noahmobile.com_15.2.291.apk'
    def __init__(self):
        self.poco = UnityPoco()
        device = connect_device(self.main_phone)
        self.width = device.get_display_info()['width']
        self.height = device.get_display_info()['height']
        list_app = device.list_app()
        if self.main_package not in list_app:
            print('安装包体中')
            device.install_app(self.package_path,self.main_package)
            start_app(self.main_package)
        else:
            print('包体已安装')
            start_app(self.main_package)
        auto_setup(__file__,logdir=True,devices=[self.main_phone])
        ST.FIND_TIMEOUT = 30   # 隐式等待
        ST.SNAPSHOT_QUALITY = 70  #图片精度

    def find(self,locator):
        return self.poco(locator)
    def find_text(self,locator):
        return self.poco(text=locator)



if __name__ == '__main__':
    MainPage()