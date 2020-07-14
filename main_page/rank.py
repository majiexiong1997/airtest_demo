'''排行榜自动化测试用例'''
from center.main_page import *
from airtest.core.api import *
from airtest.core.helper import G



from main_page.yaml_setting import yaml_load

# <airtest.core.android.android.Android object at 0x0A142970>
class rank(MainPage):

    print(MainPage)
    def rank_test(self):
        rank_list = yaml_load.yaml_load('./yaml_setting/rank.yml')

        for ranks in rank_list['rank_list']:
            print(ranks)
            self.find(ranks).click()
            toggles = self.find_chirden("ScrollViewToggle","Content")
            num_toggle = 0
            for toggle in toggles:
                num_tab = 0
                print(toggle)
                toggle.child("ImageBG").wait_for_appearance()
                toggle.child("ImageBG").click()
                view_tabs = self.find_chirden("ScrollViewTab","Content")
                num_toggle+=1
                if num_toggle == 8 :
                    print(num_toggle)
                    self.up_swipe_for_rank()
                for view_tab in view_tabs:
                    print(view_tab)
                    view_tab.child('Tab').wait_for_appearance()
                    view_tab.child('Tab').click()
                    if num_tab == 7:
                        break





if __name__ == '__main__':
    rank().rank_test()