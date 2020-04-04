# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestCheckUploadStatusInSleepMode:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 待机10分钟后唤醒屏幕，解锁后记录第一个录音文件的转写状态，循环3次。
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_check_upload_status_in_sleep_mode(self):
        for i in range(3):
            self.driver.press_keycode(26)
            time.sleep(600)
            self.driver.press_keycode(170)
            self.driver.press_keycode(170)
            time.sleep(60)
            self.driver.press_keycode(170)
            self.driver.press_keycode(170)
        self.page.local_record_page.swipe_unlock()
        time.sleep(1)
        self.page.local_record_page.swipe_unlock()
        for a in range(4):
            self.page.local_record_page.click_enter_password_to_unlock()








