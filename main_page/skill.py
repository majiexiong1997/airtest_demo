''' 技能自动化测试用例'''
from center.main_page import MainPage
from airtest.core.api import *

from center.method_cls import method_cls

method = method_cls()
class skill(MainPage):
    def test_skill(self):
        item_num = 0
        item_corp = 0
        method.wait_start_find("TextTitle")
        #  技能
        items = method.find("SkillPanel").offspring("ScrollLeft").child("Content").children()
        print(items)
        for item in items:
            # print(len(item))
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
        # items_corps = method.find("SkillPanel").offspring("ScrollLeft").child("Content").children()
        for item in range(0,3):
            method.up_swipe_by_skill()
        #战斗技能
        method.find("TabFight").click()
        corps_text = method.find("TabFight").child("Tab").offspring("Label").get_text()
        # try:
        #     assert_equal(corps_text, '战\n斗', '检查按钮文字')
        # except AssertionError:
        #     print('文字判定不对,错误字体{}'.format(corps_text))
        method.assert_type(corps_text,'战\n斗','检查按钮文字')
        method.find("TabFight").click()
        toggle_list = ["ToggleJingMale","ToggleShouMale","ToggleWanMale",
                       "ToggleYaoMale","ToggleTuiMale","ToggleJiaoMale"]
        for toggle in toggle_list:
            method.find("Viewport").offspring(toggle).child("Image").child("ImageText").click()
        viewport_list = ["ButtonFight","ButtonProperty","ButtonTips","ButtonAutoPut","ButtonTrain",
                         "ButtonOpenBag"]
        for btn in viewport_list :
            method.find("Viewport").offspring(btn).click()
            method.click_center()
            if btn == "ButtonOpenBag":
                method.find("ButtonClose").click()



        # MainPage().up_swipe_by_skill()



















if __name__ == '__main__':
    skill().test_skill()