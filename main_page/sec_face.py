from center.main_page import MainPage
from airtest.core.api import *

from main_page.yaml_setting import yaml_load


class sec_face(MainPage):
    list_sec = yaml_load.yaml_load(r'./yaml_setting/sec_face.yml')

    def sec_face_test(self):
        '''二级界面'''
        tisheng = 'ButtonGrowthTips'
        for sec_face in self.list_sec['list_sec']:
            self.find("FunctionPanel").offspring(sec_face).click()
            snapshot()
            time.sleep(5)
            self.find_click("ButtonClose")

        for sec_face in self.list_sec['list_sec_one']:
            self.find_click(sec_face)
            snapshot()
            time.sleep(5)
            self.find_click("ButtonClose")

    def character_Stats(self):
        '''人物栏'''
        self.find_click("ButtonRole")
    def Equip(self):
        # 属性
        self.find_click("ToggleEquip")
        Equip_btn = self.find_text("ToggleEquip","LabelCheck")
        self.assert_type(Equip_btn, '属\n性', '当前点击按钮检查')
    def Information(self):
        # 资料
        self.find_click("ToggleInformation")
        Information_btn = '资\n料'
        self.assert_type(Information_btn, '资\n料', '当前点击按钮检查')
    def Honor(self):
        # 积分
        self.find_click("ToggleHonor")
        Honor_btn = '积\n分'
        # Honor_btn = self.find("ToggleHonor","Label").get_text()
        # Honor_btn = self.find_text("ToggleHonor","Label")
        self.assert_type(Honor_btn, '积\n分', '当前点击按钮检查')
    def Title(self):
        # 称号
        self.find_click("ToggleTitle")
        Title_btn = '称\n号'
        self.assert_type(Title_btn, '称\n号', '当前点击按钮检查')
        # 常规称号
        self.find_click("ToggleNormalTitle")
        NormalTitle_btn = '常规称号'
        self.assert_type(NormalTitle_btn, '常规称号', '当前点击按钮检查')
        "ToggleNormalTitle"
        # 特殊称号
        self.find_click("ToggleSpecialTitle")
        Special_btn = '特殊称号'
        self.assert_type(Special_btn, '特殊称号', '当前点击按钮检查')

        return self


if __name__ == '__main__':
    sec_face().Title()
    sec_face().Equip()
    sec_face().Information()
    sec_face().Honor()


