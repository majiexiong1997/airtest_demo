import os
from airtest.core.android.adb import ADB
from airtest.aircv.keypoint_base import *
class start_time:
    main_page = 'com.sina.weibo'
    main_activity = '.MainTabActivity'
    @print_run_time
    def count_start_time(self):
        os.popen('adb shell pm clear {}'.format(self.main_page))
        os.popen('adb shell am force-stop {}'.format(self.main_page))
        #手机型号
        with os.popen('adb shell getprop ro.product.model', 'r') as p:
            phone = p.read()
        #手机启动
        with os.popen('adb shell am start -S -W {}/{}'.format(self.main_page, self.main_activity),
                      'r') as p:
            r = p.read()
        r = r.split('\n')
        start_time = r[-4]
        end_time = r[-3]
        start_time = int(start_time.split(':')[1])
        end_time = int(end_time.split(':')[1])
        count = end_time - start_time
        print('当前手机{}启动耗时{}s'.format(phone,count))


if __name__ == '__main__':
    start_time().count_start_time()




