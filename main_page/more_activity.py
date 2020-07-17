from center.main_page import MainPage

from airtest.core.api import *

class more_activity(MainPage):
    def test_activity(self):
        '''活动栏'''
        activitys = self.find_chirden('Bg','Content')
        for activity in activitys:
            activity.click()
        return self
    def test_calendar(self):
        '''日历栏'''
        self.find_click("Calendar")
        snapshot()

        pass



if __name__ == '__main__':
    more_activity().test_activity()