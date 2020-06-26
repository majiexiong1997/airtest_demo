from center.main_page import MainPage
from main_page.xuanfu import gonggao
from main_page.xuanfu import xuanfu


class Main(MainPage):
    #登录
    def login(self):
        self.find("ButtonLogin").click()
        return xuanfu()
    #公告
    def gonggao(self):
        self.find("ButtonNotice").click()
        return gonggao()
