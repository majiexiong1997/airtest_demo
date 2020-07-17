''' 技能自动化测试用例'''

from airtest.core.api import *

from center.main_page import MainPage
from main_page.yaml_setting import yaml_load


class skill(MainPage):

    def test_skill(self):
        item_num = 0
        self.find("TextTitle").wait_for_appearance()
        #  技能
        items = self.find_chirden("SkillPanel", "ScrollLeft", "Content")
        print(items)
        for item in items:
            if item_num != 0 and item_num % 4 == 0:
                self.up_swipe_by_skill()
                item.child('ImageIcon').click()
            else:
                item.child('ImageIcon').click()
            item_num += 1
        # 军团技能
        corps_text = self.find_text("TabCorps", "Tab", "Label")
        try:
            assert_equal(corps_text, '军\n团', '检查按钮文字')
        except AssertionError:
            print('文字判定不对,错误字体{}'.format(corps_text))
        self.find_click("TabCorps")
        for item in range(0, 3):
            self.up_swipe_by_skill()
        # 战斗技能
        self.find_click("TabFight")
        corps_text = self.find_text("TabFight", "Tab", "Label")
        self.assert_type(corps_text, '战\n斗', '检查按钮文字')
        self.find_click("TabFight")
        list_skill = yaml_load.yaml_load(r'./yaml_setting/skill.yml')
        for toggle in list_skill['toggle_list']:
            self.find("Viewport").offspring(toggle).child("Image").child("ImageText").click()
        for btn in list_skill['viewport_list']:
            self.find("Viewport").offspring(btn).click()
            self.click_center()
            if btn == "ButtonOpenBag":
                self.find_click("ButtonClose")

        # MainPage().up_swipe_by_skill()


if __name__ == '__main__':
    skill().test_skill()
