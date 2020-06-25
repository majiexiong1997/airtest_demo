from main_page import MainPage


class xuanfu(MainPage):
    main_package = "shangyoo.noahmobile.com"
    main_phone = "Android:///"
    def xuanfu(self):
        self.find("2").click()
        self.find("ButtonChoose").click()


