''' 技能自动化测试用例'''
from center.main_page import MainPage


class skill(MainPage):
    def test_skill(self):
        item_num = 0
        items = self.find("SkillPanel").offspring("ScrollLeft").child("Content").children()
        print(items)
        for item in items:
            # print(len(item))
            if item_num != 0 and item_num % 4 == 0:
                MainPage().up_swipe_by_skill()
                item.child('ImageIcon').click()
            else:
                item.child('ImageIcon').click()

            item_num += 1


        # MainPage().up_swipe_by_skill()



















if __name__ == '__main__':
    skill().test_skill()