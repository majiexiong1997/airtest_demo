from center.main_page import MainPage
from main_page.xuanfu import xuanfu


class Main(MainPage):

    def login(self):
        self.find("ButtonLogin").click()
        return xuanfu()
