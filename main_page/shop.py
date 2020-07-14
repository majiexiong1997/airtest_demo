from center.main_page import MainPage
from airtest.core.api import *

class shop(MainPage):


    def shop_test(self):
        #纵向标签

        y_btn = ["ToggleJinBi","ToggleYouHui","ToggleBangJin","ToggleNuoYa","ToggleRecharge"]

        for y in y_btn:
            print(y)
            self.find(y).wait_for_appearance()
            self.find(y).click()
            # 横向标签
            x_btn = self.find("UIShopMallView").child("ToggleLevel2").children()
            if y == "ToggleRecharge":
                break
            for x in x_btn:
                print(x)
                x.child('Tab').wait_for_appearance()
                x.child('Tab').click()
                # 横向子标签
                x_child_btn = self.find("UIShopMallView").child("ToggleLevel3").children()
                for x_child in x_child_btn:

                    x_child.child('Tab').wait_for_appearance()
                    x_child.child('Tab').click()
                    item_btn = self.find("ScrollView").child("ScrollPanel").children()
                    # if assert_not_exists(item_btn):
                    #     pass
                    # num = 0
                    #
                    # for item in item_btn:
                    #     item.child('Icon').wait_for_appearance()
                    #
                    #     item.child('Icon').click()
                    #     time.sleep(1)
                    #     touch(Template(r"./test_img/tpl1593762440347.png", record_pos=(0.169, -0.097), resolution=(2460, 1080)))
                    #     num +=1
                    #
                    #     if num % 8 == 0:
                    #         self.up_swipe()

        moneys = self.find("UIShopMallView").child("ToggleLevel3").children()
        for money in moneys:
            money.child('Tab').click()




        # pass













if __name__ == '__main__':
    shop().shop_test()