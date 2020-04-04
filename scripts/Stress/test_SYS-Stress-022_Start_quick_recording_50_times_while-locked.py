# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestStartOrCancelRecord:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在锁屏界面，启动快速录音50次
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_start_quick_recording_50_times_while_locked(self):
        self.driver.press_keycode(26)
        time.sleep(2)
        for i in range(50):
            self.driver.press_keycode(26)
            time.sleep(2)
            self.driver.press_keycode(170)
            self.driver.press_keycode(170)
            time.sleep(10)
            self.driver.press_keycode(170)
            self.driver.press_keycode(170)
            time.sleep(2)
            self.driver.press_keycode(26)
        self.driver.press_keycode(26)
        self.page.local_record_page.swipe_unlock()
        time.sleep(1)
        self.page.local_record_page.swipe_unlock()
        for a in range(4):
            self.page.local_record_page.click_enter_password_to_unlock()






