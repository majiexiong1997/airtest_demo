from center.main_page import MainPage
from main_page.more_activity import more_activity
from main_page.rank import rank
from main_page.skill import skill
from main_page.login import *
from main_page.sec_face import *
from main_page.bag_store import *
from main_page.group import *

method = method_cls()
class Main(MainPage):
    #登录
    def login_sec(self):
        method.find("ButtonLogin").click()
        return login()
    #首次登录
    def login_frist(self):
        return login()
    #公告
    def gonggao(self):
        method.find("ButtonNotice").click()
        return login()
    #二级界面
    def sec_face(self):
        return sec_face()
    #背包
    def bag_store(self):
        method.find('ButtonBag').click()
        return bag_store()
    #技能
    def skill(self):
        method.find('ButtonSkill').click()
        return skill()
    def rank(self):
        method.find('ButtonRank').click()
        return rank()
    def more_activity(self):
        '''更多活动'''
        method.find('ButtonMoreActivity').click()
        return more_activity()
    def group(self):
        '''成长'''
        method.find('ButtonHandbook').click()
        return group()