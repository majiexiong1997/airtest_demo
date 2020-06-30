from center.main_page import MainPage
from airtest.core.api import *


class login(MainPage):
    def quanxian(self):
        for i in range(0,5):
            touch(Template(r"./test_img/tpl1593331724433.png", record_pos=(-0.001, 0.037),
                           resolution=(self.height, self.width)))
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
        self.find("ButtonLogin").click()
        self.find("2").click()
        self.find("ButtonChoose").click()
        self.find("ButtonEnterGame").click()

    def login_frist(self):
        '''初次登录'''
        time.sleep(5)
        self.find("ButtonOK").click()
        self.find("Background1").click()
        self.find("ButtonLogin").click()
        self.find("InputFieldAccount").child("Text").click()
        text('1455080341')
        self.find("ButtonChangeAccount").click()
        self.find("InputFieldPsw").child("Text").click()
        text('Aa990223')
        touch((self.width, 0))
        self.find("UILoginAccountView").child("ButtonLogin").click()
        self.find("ButtonOK").click()
        touch(Template(r"./test_img/tpl1593330282492.png", record_pos=(-0.114, 0.165), resolution=(self.height, self.width)))
        self.find("ButtonLogin").click()
        self.find_text("更 新").click()
        text_title = self.find("TextTitle").wait_for_appearance().get_text()
        if assert_equal(text_title,'选择服务器线路','是否进入选服') == None:
            self.find("2").click()
            self.find("ButtonChoose").click()
            self.find("ButtonEnterGame").click()
            self.find("Scroll View").click()
            self.find("ButtonRole").click()
            self.find("ImageMapBG").click()
            self.find("InteractiveRegion").click()


    def sec_face(self):
        '''二级界面'''
        list_sec = ['ButtonSkill','ButtonQuest','ButtonMount','ButtonRank','ButtonMail',
                    'ButtonSetting','ButtonRemake','ButtonStrengthen','ButtonSocialSystem']
        list_sec_one = ['ButtonBag','ButtonFriend','ButtonShopMall','ButtonHandbook','ButtonMoreActivity']
        tisheng = 'ButtonGrowthTips'
        for sec_face in list_sec :
            self.find("FunctionPanel").offspring(sec_face).click()
            snapshot()
            time.sleep(5)
            self.find("ButtonClose").click()
        for sec_face in list_sec_one:
            self.find(sec_face).click()
            snapshot()
            time.sleep(5)
            self.find("ButtonClose").click()

        #cw
        # self.find(tisheng).click()
        # self.find("1").click()
        # self.find("ButtonClose").click()
        # self.find("2").click()
        # self.find("ButtonClose").click()
class gonggao(MainPage):
    def gonggao(self):
        gonggao_btn = self.find("ButtonOk").child("Text")
        gonggao_ass = gonggao_btn.attr('text')
        if assert_equal(gonggao_ass,'我知道了','测试是否打开公告') == None:
            self.find("ButtonOk").click()


if __name__ == '__main__':

    login().sec_face()




