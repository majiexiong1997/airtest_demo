import time

from airtest.core.api import connect_device
main_phone = "Android:///"
device = connect_device(main_phone)

if device.check_app('shangyoo.noahmobile.com') == False:
    pass
    print('error')
    device.install_app('111')
    device.start_app('111')
    device_act = device.get_top_activity_name()
    # device.start_app_timing('111', device_act)

else:
        print('包体已安装到手机中')
        device.start_app('shangyoo.noahmobile.com')

        # device_act = device.get_top_activity_name()
        # device_act = device_act.split('/')[-1]


        # start_time = device.start_app_timing('shangyoo.noahmobile.com','com.tpf.sdk.unity.TPFUnityContext')






