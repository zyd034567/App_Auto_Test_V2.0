# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLockAndUnLockDuringRecordingInStandardMode:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在标准模式下录音30分钟，录音过程中锁屏并解锁
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_lock_and_unlock_during_recording_in_standard_mode(self):
        self.page.local_record_page.click_standard()
        time.sleep(10)
        for i in range(30):
            time.sleep(20)
            self.driver.press_keycode(26)
            time.sleep(2)
            self.driver.press_keycode(26)
            self.page.local_record_page.swipe_unlock()
            time.sleep(1)
            self.page.local_record_page.swipe_unlock()
            for a in range(4):
                self.page.local_record_page.click_enter_password_to_unlock()
            time.sleep(30)
        self.page.record_translate_while_recording_page.click_continue_transfer()
        self.page.record_page.click_accomplish()
        self.page.record_page.click_save()
