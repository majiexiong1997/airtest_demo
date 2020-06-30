from center.main_page import MainPage
from airtest.core.api import *



class bag_store(MainPage):
    def bag(self):
        self.find("ToggleTask").child("TabSelect").click()
        self.find("ToggleNormal").child("TabSelect").click()
        self.find("TogglePage1").click()
        self.find("TogglePage2").click()
        self.find("TogglePage3").click()
        self.find("TogglePage1").click()
        self.find("ButtonZhengLi").click()
        self.find("ButtonBaiTan").click()
        self.find("ButtonDuiHuanYingBi").click()
        self.find("ButtonClose").click()
        self.find("ButtonLock").click()
        self.find("ButtonClose").click()
        list_zb = [i for i in range(0,14)]
        for zb_click in list_zb:
            self.find("UIEquipBagView").child("Content").offspring('{}'.format(zb_click)).click()
        list_goods = [i for i in range(0,47)]
        for goods_click in list_goods:
            self.find('Bag').child("Content").offspring('{}'.format(goods_click)).click()
            if goods_click >= 33 and goods_click <=34:
                # 向上滑动
                MainPage().up_swipe()





    def store(self):
        pass



if __name__ == '__main__':
    bag_store().bag()