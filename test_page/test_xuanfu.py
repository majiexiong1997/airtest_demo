from center.main_page import MainPage

import pytest


from main_page.main import Main


class Testxuanfu:
    def setup(self):
        self.main = Main()

    def test_login_frist(self):
        self.main = Main().login_frist().login_frist()
    def test_login_sec(self):
        self.main = Main().login_sec().login_sec()
    def test_gonggao(self):
        self.main = Main().gonggao().gonggao()
    def test_sec_face(self):
        self.main = Main().sec_face().sec_face()




if __name__ == '__main__':
    Testxuanfu().test_login_sec()