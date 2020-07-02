from center.main_page import MainPage
from airtest.core.api import *

from center.method_cls import method_cls

method = method_cls()
class login(MainPage):
    def quanxian(self):
        for i in range(0,5):
            touch(Template(r"./test_img/tpl1593331724433.png", record_pos=(-0.001, 0.037),
                           resolution=(method.screeen_size())))
            # touch(Template(r"./test_img/tpl1593331724433.png", record_pos=(-0.001, 0.037),
            #                resolution=(self.height, self.width)))
            # touch(Template(r"./test_img/tpl1593331724433.png", record_pos=(-0.001, 0.037),
            #                resolution=(self.height, self.width)))
            # touch(Template(r"./test_img/tpl1593331724433.png", record_pos=(-0.001, 0.037),
            #                resolution=(self.height, self.width)))
            # touch(Template(r"./test_img/tpl1593331724433.png", record_pos=(-0.001, 0.037),
            #                resolution=(self.height, self.width)))


    def login_sec(self):
        '''已有账号登录'''
        method.find("ButtonLogin").click()
        method.find("2").click()
        method.find("ButtonChoose").click()
        method.find("ButtonEnterGame").click()

    def login_frist(self):
        '''初次登录'''
        time.sleep(5)
        method.find("ButtonOK").click()
        method.find("Background1").click()
        method.find("ButtonLogin").click()
        method.find("InputFieldAccount").child("Text").click()
        text('1455080341')
        method.find("ButtonChangeAccount").click()
        method.find("InputFieldPsw").child("Text").click()
        text('Aa990223')
        touch((method.screeen_size()[0], 0))
        method.find("UILoginAccountView").child("ButtonLogin").click()
        method.find("ButtonOK").click()
        touch(Template(r"./test_img/tpl1593330282492.png", record_pos=(-0.114, 0.165), resolution=(self.height, self.width)))
        method.find("ButtonLogin").click()
        method.find_text("更 新").click()
        text_title = method.find("TextTitle").wait_for_appearance().get_text()
        if assert_equal(text_title,'选择服务器线路','是否进入选服') == None:
            method.find("2").click()
            method.find("ButtonChoose").click()
            method.find("ButtonEnterGame").click()
            method.find("Scroll View").click()
            method.find("ButtonRole").click()
            method.find("ImageMapBG").click()
            method.find("InteractiveRegion").click()


    def sec_face(self):
        '''二级界面'''
        list_sec = ['ButtonSkill','ButtonQuest','ButtonMount','ButtonRank','ButtonMail',
                    'ButtonSetting','ButtonRemake','ButtonStrengthen','ButtonSocialSystem']
        list_sec_one = ['ButtonBag','ButtonFriend','ButtonShopMall','ButtonHandbook','ButtonMoreActivity']
        tisheng = 'ButtonGrowthTips'
        for sec_face in list_sec :
            method.find("FunctionPanel").offspring(sec_face).click()
            snapshot()
            time.sleep(5)
            method.find("ButtonClose").click()
        for sec_face in list_sec_one:
            method.find(sec_face).click()
            snapshot()
            time.sleep(5)
            method.find("ButtonClose").click()

        #cw
        # method.find(tisheng).click()
        # method.find("1").click()
        # method.find("ButtonClose").click()
        # method.find("2").click()
        # method.find("ButtonClose").click()
class gonggao(MainPage):
    def gonggao(self):
        gonggao_btn = method.find("ButtonOk").child("Text")
        gonggao_ass = gonggao_btn.attr('text')
        try:
            assert_equal(gonggao_ass,'我知道了','测试是否打开公告')
        except AssertionError:
            print('文字判定不对,错误字体{}'.format(gonggao_ass))
        method.find("ButtonOk").click()


if __name__ == '__main__':

    login().sec_face()




