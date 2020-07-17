from center.main_page import MainPage

import pytest
from center.main_page import *

from main_page.main import Main

from airtest.aircv.keypoint_base import *
class TestXuanfu:
    '''总控'''
    def setup(self):
        self.main = Main()
    # def test_login_frist(self):
    #     self.main = Main().login_frist().login_frist()
    # def test_login_sec(self):
    #     self.main = Main().login_sec().login_sec()
    # def test_gonggao(self):
    #     self.main = Main().gonggao().gonggao()
    # def test_sec_face(self):
    #     self.main = Main().sec_face().sec_face()
    # def test_skill(self):
    #     self.main = Main().skill().test_skill()
    @print_run_time

    def test_group(self):
        self.main = Main().group().target().active().referrals().getback().other().today()
    def teardown(self):
        pass
        # MainPage().report()

        # MainPage().stop_app()




