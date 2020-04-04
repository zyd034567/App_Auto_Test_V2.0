# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestTurnOffTheScreenAndStartRecordingFast50Times:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在灭屏待机状态下，启动快速录音50次
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_turn_off_the_screen_and_start_recording_fast_50_times(self):
        for i in range(50):
            self.driver.press_keycode(26)
            time.sleep(5)
            self.driver.press_keycode(170)
            self.driver.press_keycode(170)
            time.sleep(10)
            self.driver.press_keycode(170)
            self.driver.press_keycode(170)
        time.sleep(1)
        self.page.local_record_page.swipe_unlock()
        time.sleep(1)
        self.page.local_record_page.swipe_unlock()
        for a in range(4):
            self.page.local_record_page.click_enter_password_to_unlock()






