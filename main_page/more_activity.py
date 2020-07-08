from center.main_page import MainPage
from center.method_cls import *
from airtest.core.api import *
method = method_cls()
class more_activity(MainPage):
    #活动栏
    def test_activity(self):
        activitys = method.find('Bg').child('Content').children()
        for activity in activitys:
            activity.click()
        return self
    #日历栏
    def test_calendar(self):
        method.find("Calendar").click()
        snapshot()

        pass



if __name__ == '__main__':
    more_activity().test_activity()