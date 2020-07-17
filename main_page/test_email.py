from center.main_page import MainPage
from airtest.core.api import *

from main_page.yaml_setting import yaml_load


class Email(MainPage):
    '''邮件自动化用例'''

    def test_friend(self):
        '''好友 "TabFriend"'''
        self.find_click("TabFriend")
        friend_btn = self.find_text("TabFriend", 'Tab', 'Label')
        self.assert_type(friend_btn, '好\n友', '当前点击按钮检查')
        return self

    def test_temporary(self):
        '''临时 "TabTemp"'''
        self.find_click("TabTemp")
        temporary_btn = self.find_text("TabTemp", 'Tab', 'Label')
        self.assert_type(temporary_btn, '临\n时', '当前点击按钮检查')
        return self

    def test_group_chat(self):
        '''群聊 "TabGroup"'''
        self.find_click("TabGroup")
        temporary_btn = self.find_text("TabGroup", 'Tab', 'Label')
        self.assert_type(temporary_btn, '群\n聊', '当前点击按钮检查')
        return self

    def test_email(self):
        '''邮件 "TabMail"'''
        self.find_click("TabMail")
        temporary_btn = self.find_text("TabMail", 'Tab', 'Label')
        self.assert_type(temporary_btn, '邮\n件', '当前点击按钮检查')
        return self


if __name__ == '__main__':
    Email().test_email()
    Email().test_friend()
    Email().test_group_chat()
    Email().test_temporary()