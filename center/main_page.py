import traceback

from airtest.core.android.adb import ADB
from airtest.core.api import *
import os
from poco.drivers.unity3d import UnityPoco
from airtest.cli.parser import cli_setup
from airtest.core.android.android import Android




class MainPage:
    main_package = "xxx"
    main_phone = "Android:///"
    package_path = r'xxx'

    def __init__(self):
        adb = ADB()
        device_list = adb.devices()
        deviceNum = len(device_list) >= 1
        assert_equal(deviceNum, True, "设备连接数量至少为1台以上")
        for i in range(len(device_list)):
            self.device = connect_device(self.main_phone)

            device = self.device
            if not cli_setup():
                auto_setup(__file__, logdir=False, devices=[self.main_phone+device_list[i][0]])
            list_app = device.list_app()
            if self.main_package not in list_app:
                print('安装包体中')
                device.install_app(self.package_path,self.main_package)
                start_app(self.main_package)
                time.sleep(10)
                self.poco = UnityPoco()
            else:
                print('包体已安装')

                start_app(self.main_package)
                time.sleep(10)
                self.poco = UnityPoco()
                ST.FIND_TIMEOUT = 30  # 隐式等待
                ST.SNAPSHOT_QUALITY = 70  # 图片精度



















if __name__ == '__main__':
    MainPage()


