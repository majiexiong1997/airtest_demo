from center.main_page import MainPage
from main_page.xuanfu import gonggao
from main_page.xuanfu import *
from main_page.bag_store import *


class Main(MainPage):
    #登录
    def login_sec(self):
        self.find("ButtonLogin").click()
        return login()
    #首次登录
    def login_frist(self):
        return login()
    #公告
    def gonggao(self):
        self.find("ButtonNotice").click()
        return gonggao()
    def sec_face(self):
        return login()
    def bag_store(self):
        self.find('ButtonBag').click()
        return bag_store()
