from center.main_page import MainPage

from center.main_page import MainPage
from airtest.core.api import *

from center.method_cls import method_cls
from main_page.yaml_setting import yaml_load
method = method_cls()
class login(MainPage):

    def quanxian(self):
        for i in range(0,5):
            touch(Template(r"./test_img/tpl1593331724433.png", record_pos=(-0.001, 0.037),
                           resolution=(method.screeen_size())))

    def login_sec(self):
        '''二次登录'''
        method.find_click("ButtonLogin")
        if exists(Template(r"./test_img/tpl1594179066201.png", record_pos=(-0.0, -0.169), resolution=(method.screeen_size()))):
            touch(Template(r"./test_img/tpl1594179100541.png", record_pos=(0.001, 0.162), resolution=(method.screeen_size())))
        if exists(Template(r"./test_img/tpl1594178390896.png", record_pos=(-0.001, 0.03), resolution=(method.screeen_size()))):
            touch(Template(r"./test_img/tpl1594178390896.png", record_pos=(-0.001, 0.03), resolution=(method.screeen_size())))
        if method.find("2").exists():
            method.find_click("2")
            method.find_click("ButtonChoose")
        method.find_click("ButtonEnterGame")
        return self

    def login_frist(self):
        '''首次登录'''
        if exists(Template(r"./test_img/tpl1594179425880.png", record_pos=(-0.002, -0.168), resolution=(method.screeen_size()))):
            touch(Template(r"./test_img/tpl1594179460930.png", record_pos=(0.122, 0.163), resolution=(method.screeen_size())))
        method.find_click("ButtonLogin")
        method.find_click("InputFieldAccount","Text")
        text('1455080341')
        method.find_click("ButtonChangeAccount")
        method.find_click("InputFieldPsw","Text")
        text('Aa990223')
        touch(Template(r"./test_img/tpl1594177890833.png", record_pos=(0.384, -0.109),
                       resolution=(method.screeen_size())))
        method.find_click("ButtonLogin")
        method.find_click("UILoginAccountView","ButtonLogin")
        if exists(Template(r"./test_img/tpl1594178390896.png", record_pos=(-0.001, 0.03), resolution=(method.screeen_size()))):
            touch(Template(r"./test_img/tpl1594178390896.png", record_pos=(-0.001, 0.03), resolution=(method.screeen_size())))
        touch(Template(r"./test_img/tpl1593330282492.png", record_pos=(-0.114, 0.165),
                       resolution=(method.screeen_size())))
        method.find_click("ButtonLogin")
        if exists(Template(r"./test_img/tpl1594178802784.png", record_pos=(-0.059, 0.03), resolution=(method.screeen_size()))):
            touch(Template(r"./test_img/tpl1594178802784.png", record_pos=(-0.059, 0.03), resolution=(method.screeen_size())))
        method.find_click("ButtonLogin")
        if exists(Template(r"./test_img/tpl1594179066201.png", record_pos=(-0.0, -0.169), resolution=(method.screeen_size()))):
            touch(Template(r"./test_img/tpl1594179100541.png", record_pos=(0.001, 0.162), resolution=(method.screeen_size())))
        method.find_click("2")
        method.find_click("ButtonChoose")
        ''''''
        method.find_click("ButtonEnterGame")
        method.find("ChatPanel").child("ImageBG").click()
        method.find("ButtonRole").click()
        method.find("ImageMapBG").click()
        method.find("InteractiveRegion").click()
        return self

    def gonggao(self):
        '''公告'''
        gonggao_btn = method.find("ButtonOk").child("Text").attr('text')

        try:
            assert_equal(gonggao_btn,'我知道了','测试是否打开公告')
        except AssertionError:
            print('文字判定不对,错误字体{}'.format(gonggao_btn))
        method.find("ButtonOk").click()
        return self
    def download(self):
        '''扩展包下载'''
        method.find("ButtonExResource").click()
        method.find("ButtonYes").click()
        method.wait_start_find("ButtonYes")
        method.find("ButtonYes").click()
        start_app(self.main_package)
        method.wait_start_find("ButtonServer")
        return self
    def support(self):
        '''客服'''
        method.find("ButtonService").click()
        start_app(self.main_package)

        return self
    def change_login(self):
        '''切换账户'''
        method.find("ButtonChangeAccount").click()
        method.find("ButtonBack").click()
        method.find("ButtonChangeAccount").click()
        method.find("ButtonLogin").click()
        return self
    def create_role(self):
        '''创建角色'''
        method.find("3").click()
        role_list = ["JwsCB","YnzCB","QxsCB","GdjCB","LmrCB","SwzCB","TqzCB","SdkCB"]
        for role in role_list:
            method.find(role).click()
            method.find("ChoSex_Male").click()
            method.find("ChoSex_Female").click()
        method.find("RdmNameBtn").click()
        method.find("OkBtn").click()

        method.wait_start_find("ButtonEnterGame")
        method.find("ButtonEnterGame").click()
        if method.find("ChatPanel").child("ImageBG").exists():
            method.find("ChatPanel").child("ImageBG").click()
            method.find("ButtonRole").click()
            method.find("ImageMapBG").click()
            method.find("InteractiveRegion").click()
        return self











if __name__ == '__main__':
    login().support()