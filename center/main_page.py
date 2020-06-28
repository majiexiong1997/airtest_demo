from airtest.core.api import *
import os
from poco.drivers.unity3d import UnityPoco

from airtest.core.android.android import Android




class MainPage:
    main_package = "shangyoo.noahmobile.com"
    main_phone = "Android:///"
    def __init__(self):
        self.poco = UnityPoco()

        device = connect_device(self.main_phone)
        device.list_app(third_only=True)

        # if "shangyoo.noahmobile.com" not in device:
        #     os.popen("adb install -r ")
        start_app(self.main_package)
        auto_setup(__file__,logdir=True,devices=[self.main_phone])

    def find(self,locator):
        return self.poco(locator)



if __name__ == '__main__':
    MainPage()