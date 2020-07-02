from center.main_page import MainPage
from airtest.core.api import *
from center.method_cls import *
from main_page.yaml_setting import yaml_load

method = method_cls()
class bag_store(MainPage):
    '''背包自动化测试用例'''
    def bag(self):
        method.find("ToggleTask").child("TabSelect").click()
        method.find("ToggleNormal").child("TabSelect").click()
        bags = yaml_load.yaml_load(r'./yaml_setting/bag.yml')
        for bag in bags['bag']:
            method.find(bag).click()
        list_zb = [i for i in range(0,14)]
        for zb_click in list_zb:
            method.find("UIEquipBagView").child("Content").offspring('{}'.format(zb_click)).click()
        list_goods = [i for i in range(0,47)]
        for goods_click in list_goods:
            method.find('Bag').child("Content").offspring('{}'.format(goods_click)).click()
            if goods_click >= 33 and goods_click <=34:
                # 向上滑动
                method.up_swipe()





    def store(self):
        pass



if __name__ == '__main__':
    bag_store().bag()