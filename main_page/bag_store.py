import traceback

from center.main_page import MainPage
from airtest.core.api import *
from main_page.yaml_setting import yaml_load


class bag_store(MainPage):
    '''背包自动化测试用例'''

    def bag(self):
        self.find_click("ToggleTask", "TabSelect")
        self.find_click("ToggleNormal", "TabSelect")
        bags = yaml_load.yaml_load(r'./yaml_setting/bag.yml')
        for bag in bags['bag']:
            self.find(bag).click()
        list_zb = self.find("UIEquipBagView").offspring("Content")[0].children()
        for zb_click in list_zb:
            zb_click.child("Icon").click()
        list_goods = self.find("UIEquipBagView").offspring("Content")[1].children()
        js_num = 0
        for goods_click in list_goods:
            goods_click.child("Icon").click()
            if js_num == 8:
                self.find_click("ButtonCancel")
            if js_num >= 33 and js_num <= 34:
                # 向上滑动
                self.up_swipe()
            js_num += 1

    def store(self):
        pass


if __name__ == '__main__':
    bag_store().bag()
