from center.main_page import MainPage
from airtest.core.api import *


class xuanfu(MainPage):

    def xuanfu(self):
        self.find("2").click()
        self.find("ButtonChoose").click()

class gonggao(MainPage):
    def gonggao(self):
        gonggao_btn = self.find("ButtonOk").child("Text")
        gonggao_ass = gonggao_btn.attr('text')
        if assert_equal(gonggao_ass,'我知道了','测试是否打开公告') == None:
            self.find("ButtonOk").click()







if __name__ == '__main__':
    gonggao().gonggao()



