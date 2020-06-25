from airtest.core.api import *
import os
from poco.drivers.unity3d import UnityPoco
class MainPage:
    main_package = ""
    main_phone = ""
    def __init__(self):
        self.poco = UnityPoco()
        connect_device(self.main_phone)
        if self.main_package != "":
            start_app(self.main_package)
            auto_setup(__file__,logdir=True,devices=[self.main_phone])

    def find(self,locator):
        return self.poco(locator)



