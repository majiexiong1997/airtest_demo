from center.main_page import MainPage

import pytest


from main_page.main import Main


class Testxuanfu:
    def setup(self):
        self.main = Main()

    def test_xuanfu(self):
        self.main = Main().login()
    def test_gonggao(self):
        self.main = Main().gonggao().gonggao()



if __name__ == '__main__':
    Testxuanfu().test_gonggao()