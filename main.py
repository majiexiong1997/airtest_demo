from main_page import MainPage
from xuanfu import xuanfu


class Main(MainPage):
    main_package = "shangyoo.noahmobile.com"
    main_phone = "Android:///"
    def login(self):
        self.find("ButtonLogin").click()
        return xuanfu()
