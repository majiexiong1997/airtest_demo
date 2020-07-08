from center.main_page import MainPage
from airtest.core.api import *

from center.method_cls import method_cls
from main_page.yaml_setting import yaml_load
method = method_cls()
class sec_face(MainPage):
    def sec_face(self):
        '''二级界面'''
        list_sec = yaml_load.yaml_load(r'./yaml_setting/sec_face.yml')
        tisheng = 'ButtonGrowthTips'
        for sec_face in list_sec['list_sec'] :
            method.find("FunctionPanel").offspring(sec_face).click()
            snapshot()
            time.sleep(5)
            method.find("ButtonClose").click()
        for sec_face in list_sec['list_sec_one']:
            method.find(sec_face).click()
            snapshot()
            time.sleep(5)
            method.find("ButtonClose").click()