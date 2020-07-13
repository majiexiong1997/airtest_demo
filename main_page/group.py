
from center.main_page import *
from airtest.core.api import *
from airtest.core.helper import G




class group(MainPage):

    def active(self):
        '''活动按钮'''
        self.find_click("TabActivity")
        active_btn = self.find_text("TabActivity", 'Tab', 'Label')
        self.assert_type(active_btn,'活\n跃','当前点击按钮检查')
        return self
    def referrals(self):
        '''推荐按钮'''
        self.find_click("TabRecommend")
        referrals_btn = self.find_text("TabRecommend", 'Tab', 'Label')
        self.assert_type(referrals_btn, '推\n荐', '当前点击按钮检查')
        return self
    def today(self):
        '''今日按钮'''
        self.find_click("TabTime")
        today_btn = self.find_text("TabTime", 'Tab', 'Label')
        self.assert_type(today_btn, '今\n日', '当前点击按钮检查')
        return self
    def getback(self):
        '''找回按钮'''
        self.find_click("TabRegetBack")
        getback_btn = self.find_text("TabRegetBack", 'Tab', 'Label')
        self.assert_type(getback_btn, '找\n回', '当前点击按钮检查')
        return self
    def other(self):
        '''其他按钮'''
        self.find_click("TabOther")
        other_btn = self.find_text("TabOther", 'Tab', 'Label')
        self.assert_type(other_btn, '其\n他', '当前点击按钮检查')
        return self
    def target(self):
        '''成长按钮'''
        self.find_click("TabTarget")
        target_btn = self.find_text("TabTarget", 'Tab', 'Label')
        self.assert_type(target_btn, '成\n长', '当前点击按钮检查')
        return self


if __name__ == '__main__':
    group = group()
    group.today()
    group.other()
    group.active()
    group.target()
    group.getback()
    group.referrals()
