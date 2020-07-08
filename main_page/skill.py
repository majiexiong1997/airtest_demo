''' 技能自动化测试用例'''
from center.main_page import MainPage
from airtest.core.api import *

from center.method_cls import method_cls
from main_page.yaml_setting import yaml_load

method = method_cls()
class skill(MainPage):
    def test_skill(self):
        item_num = 0

        method.wait_start_find("TextTitle")
        #  技能
        items = method.find("SkillPanel").offspring("ScrollLeft").child("Content").children()
        print(items)
        for item in items:
            if item_num != 0 and item_num % 4 == 0:
                method.up_swipe_by_skill()
                item.child('ImageIcon').click()
            else:
                item.child('ImageIcon').click()
            item_num += 1
        #军团技能
        corps_text = method.find("TabCorps").child("Tab").offspring("Label").get_text()
        try:
            assert_equal(corps_text,'军\n团','检查按钮文字')
        except AssertionError:
            print('文字判定不对,错误字体{}'.format(corps_text))
        method.find("TabCorps").click()
        for item in range(0,3):
            method.up_swipe_by_skill()
        #战斗技能
        method.find("TabFight").click()
        corps_text = method.find("TabFight").child("Tab").offspring("Label").get_text()

        method.assert_type(corps_text,'战\n斗','检查按钮文字')
        method.find("TabFight").click()
        list_skill = yaml_load.yaml_load(r'./yaml_setting/bag.yml')
        for toggle in list_skill['toggle_list']:
            method.find("Viewport").offspring(toggle).child("Image").child("ImageText").click()
        for btn in list_skill['viewport_list'] :
            method.find("Viewport").offspring(btn).click()
            method.click_center()
            if btn == "ButtonOpenBag":
                method.find("ButtonClose").click()



        # MainPage().up_swipe_by_skill()



















if __name__ == '__main__':
    skill().test_skill()