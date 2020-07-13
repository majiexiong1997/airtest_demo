from center.main_page import MainPage

from center.main_page import MainPage
from airtest.core.api import *


from main_page.yaml_setting import yaml_load

class login(MainPage):


    def quanxian(self):
        for i in range(0,5):
            touch(Template(r"./test_img/tpl1593331724433.png", record_pos=(-0.001, 0.037),
                           resolution=(self.screeen_size())))

    def login_sec(self):
        '''二次登录'''
        self.find_click("ButtonLogin")
        if exists(Template(r"./test_img/tpl1594179066201.png", record_pos=(-0.0, -0.169), resolution=(self.screeen_size()))):
            touch(Template(r"./test_img/tpl1594179100541.png", record_pos=(0.001, 0.162), resolution=(self.screeen_size())))
        if exists(Template(r"./test_img/tpl1594178390896.png", record_pos=(-0.001, 0.03), resolution=(self.screeen_size()))):
            touch(Template(r"./test_img/tpl1594178390896.png", record_pos=(-0.001, 0.03), resolution=(self.screeen_size())))
        if self.find("2").exists():
            self.find_click("2")
            self.find_click("ButtonChoose")
        self.find_click("ButtonEnterGame")
        return self

    def login_frist(self):
        '''首次登录'''
        if exists(Template(r"./test_img/tpl1594179425880.png", record_pos=(-0.002, -0.168), resolution=(self.screeen_size()))):
            touch(Template(r"./test_img/tpl1594179460930.png", record_pos=(0.122, 0.163), resolution=(self.screeen_size())))
        self.find_click("ButtonLogin")
        self.find_click("InputFieldAccount","Text")
        text('1455080341')
        self.find_click("ButtonChangeAccount")
        self.find_click("InputFieldPsw","Text")
        text('Aa990223')
        touch(Template(r"./test_img/tpl1594177890833.png", record_pos=(0.384, -0.109),
                       resolution=(self.screeen_size())))
        self.find_click("ButtonLogin")
        self.find_click("UILoginAccountView","ButtonLogin")
        if exists(Template(r"./test_img/tpl1594178390896.png", record_pos=(-0.001, 0.03), resolution=(self.screeen_size()))):
            touch(Template(r"./test_img/tpl1594178390896.png", record_pos=(-0.001, 0.03), resolution=(self.screeen_size())))
        touch(Template(r"./test_img/tpl1593330282492.png", record_pos=(-0.114, 0.165),
                       resolution=(self.screeen_size())))
        self.find_click("ButtonLogin")
        if exists(Template(r"./test_img/tpl1594178802784.png", record_pos=(-0.059, 0.03), resolution=(self.screeen_size()))):
            touch(Template(r"./test_img/tpl1594178802784.png", record_pos=(-0.059, 0.03), resolution=(self.screeen_size())))
        self.find_click("ButtonLogin")
        if exists(Template(r"./test_img/tpl1594179066201.png", record_pos=(-0.0, -0.169), resolution=(self.screeen_size()))):
            touch(Template(r"./test_img/tpl1594179100541.png", record_pos=(0.001, 0.162), resolution=(self.screeen_size())))
        self.find_click("2")
        self.find_click("ButtonChoose")
        ''''''
        self.find_click("ButtonEnterGame")
        self.find("ChatPanel").child("ImageBG").click()
        self.find("ButtonRole").click()
        self.find("ImageMapBG").click()
        self.find("InteractiveRegion").click()
        return self

    def gonggao(self):
        '''公告'''
        gonggao_btn = self.find("ButtonOk").child("Text").attr('text')

        try:
            assert_equal(gonggao_btn,'我知道了','测试是否打开公告')
        except AssertionError:
            print('文字判定不对,错误字体{}'.format(gonggao_btn))
        self.find("ButtonOk").click()
        return self
    def download(self):
        '''扩展包下载'''
        self.find("ButtonExResource").click()
        self.find("ButtonYes").click()
        self.wait_start_find("ButtonYes")
        self.find("ButtonYes").click()
        start_app(self.main_package)
        self.wait_start_find("ButtonServer")
        return self
    def support(self):
        '''客服'''
        self.find("ButtonService").click()
        start_app(self.main_package)

        return self
    def change_login(self):
        '''切换账户'''
        self.find("ButtonChangeAccount").click()
        self.find("ButtonBack").click()
        self.find("ButtonChangeAccount").click()
        self.find("ButtonLogin").click()
        return self
    def create_role(self):
        '''创建角色'''
        self.find("3").click()
        role_list = ["JwsCB","YnzCB","QxsCB","GdjCB","LmrCB","SwzCB","TqzCB","SdkCB"]
        for role in role_list:
            self.find(role).click()
            self.find("ChoSex_Male").click()
            self.find("ChoSex_Female").click()
        self.find("RdmNameBtn").click()
        self.find("OkBtn").click()

        self.wait_start_find("ButtonEnterGame")
        self.find("ButtonEnterGame").click()
        if self.find("ChatPanel").child("ImageBG").exists():
            self.find("ChatPanel").child("ImageBG").click()
            self.find("ButtonRole").click()
            self.find("ImageMapBG").click()
            self.find("InteractiveRegion").click()
        return self











if __name__ == '__main__':
    login().support()