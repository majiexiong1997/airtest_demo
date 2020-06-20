# -*- encoding=utf8 -*-
import pytest
import yaml

from airtest.core.api import *
import tkinter
from airtest.report.report import simple_report
import os
import poco
class TestDemo():
    def setup(self):
        __author__ = "Administrator"
        connect_device("Android:///")
        start_app("shangyoo.noahmobile.com")
        #隐式等待
        ST.FIND_TIMEOUT = 30

    def teardown(self):
        #强行等待
        time.sleep(10)
        stop_app("shangyoo.noahmobile.com")
        auto_setup(__file__)
    def get_screen(self):
        '''获取当前手机屏幕尺寸'''
        readdevice_info = os.popen('adb shell wm size').read()
        readdevice_info.split()[2].split('x')
        self.width = int(readdevice_info.split()[2].split('x')[0])
        self.height = int(readdevice_info.split()[2].split('x')[1])
    def loding_yml(self):
        self.list_load = []
        self.cfg = yaml.safe_load(open("./test_img/test_img.yml"))
        print(self.cfg['touch'])
        for i in self.cfg['touch']:
            print(i)
            self.list_load.append(i)


    @pytest.mark.parametrize()
    def test_demo(self):
        self.get_screen()

        touch(Template(r"./test_img/tpl1592614959837.png", record_pos=(0.026, 0.128), resolution=(self.height,self.width)))
        touch(Template(r"./test_img/tpl1592614993517.png", record_pos=(0.028, -0.055), resolution=(self.height,self.width)))
        touch(Template(r"./test_img/tpl1592615003933.png", record_pos=(0.032, 0.171), resolution=(self.height,self.width)))
        #显示等待
        wait(Template(r"./test_img/tpl1592615016479.png", record_pos=(-0.318, -0.189), resolution=(self.height,self.width)),timeout=10)
        touch(Template(r"./test_img/tpl1592615023379.png", record_pos=(0.42, 0.189), resolution=(self.height,self.width)))


# logapth = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'log')




