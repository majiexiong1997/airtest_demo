from airtest.core.api import *
import os
from poco.drivers.unity3d import UnityPoco

from airtest.core.android.android import Android




class MainPage:
    main_package = "xxx"
    main_phone = "Android:///"
    package_path = r'xxx'

    def __init__(self):


                self.device = connect_device(self.main_phone)
                auto_setup(__file__, logdir=False, devices=[self.main_phone])

                list_app = self.device.list_app()
                if self.main_package not in list_app:
                    print('安装包体中')
                    self.device.install_app(self.package_path,self.main_package)
                    start_app(self.main_package)
                    time.sleep(10)
                    self.poco = UnityPoco()
                else:
                    print('包体已安装')
                    start_app(self.main_package)
                    time.sleep(10)
                    self.poco = UnityPoco()
                ST.FIND_TIMEOUT = 30   # 隐式等待
                ST.SNAPSHOT_QUALITY = 70  #图片精度




if __name__ == '__main__':
    MainPage()

