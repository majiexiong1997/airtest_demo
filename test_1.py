import time
from airtest.core.api import *
from airtest.core.api import connect_device
import yaml
from airtest.core.android import adb
from center.method_cls import *
# C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\airtest\core\android\adb.py
# C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\airtest\core\android\android.py
# from airtest.report.report import simple_report
# simple_report(__file__,logpath=r'./center/log',output='./center/log/log.html')
# list_zb = [i for i in range(0,100)]
# num1 = 0
# for i in range(0,101): num1 = num1 + i ;print(num1)

# a = method_cls().screeen_size()[0]
# print(a)#
from main_page.main import method

bag_sets = method.yaml_load(open(r'main_page/yaml_setting\bag.yml'))
for bag_set in bag_sets['bag']:
    print(bag_set)
# if device.check_app('shangyoo.noahmobile.com') == False:
#     pass
#     print('error')
#     device.install_app('111')
#     device.start_app('111')
#     device_act = device.get_top_activity_name()
#     # device.start_app_timing('111', device_act)
#
# else:
#         print('包体已安装到手机中')
#         device.start_app('shangyoo.noahmobile.com')

        # device_act = device.get_top_activity_name()
        # device_act = device_act.split('/')[-1]


        # start_time = device.start_app_timing('shangyoo.noahmobile.com','com.tpf.sdk.unity.TPFUnityContext')






