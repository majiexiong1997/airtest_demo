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
        start_app(self.main_package)
        auto_setup(__file__,logdir=True,devices=[self.main_phone])

    def find(self,locator):
        return self.poco(locator)



if __name__ == '__main__':
    MainPage()