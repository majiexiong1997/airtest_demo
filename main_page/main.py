from center.main_page import MainPage
from main_page.more_activity import more_activity

from main_page.rank import rank
from main_page.skill import skill
from main_page.login import *
from main_page.sec_face import *
from main_page.bag_store import *
from main_page.group import *
from main_page.test_email import *


class Main(MainPage):

    def sec_face(self):
        '''二级界面'''
        return sec_face()

    def bag_store(self):
        '''背包'''
        self.find_click('ButtonBag')
        return bag_store()

    def skill(self):
        '''技能'''
        self.find_click('ButtonSkill')
        return skill()

    def rank(self):
        '''排行榜'''
        self.find_click('ButtonRank')
        return rank()

    def more_activity(self):
        '''更多活动'''
        self.find_click('ButtonMoreActivity')
        return more_activity()

    def group(self):
        '''成长'''
        self.find_click('ButtonHandbook')
        return group()

    def email(self):
        '''邮件'''
        self.find_click("ButtonMail")
        return Email()


if __name__ == '__main__':
    sec_face().sec_face_test()
