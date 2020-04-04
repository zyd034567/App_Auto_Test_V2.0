# coding=utf-8
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLockAndUnlockDuringRecordingEnglishInTranslateMode:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # 在主屏进入边录边译，在英文录音过程中，锁屏并解锁，查看转写和翻译内容
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_lock_and_unlock_during_recording_english_in_translate_mode(self):
        self.page.local_record_page.click_navigation_bar_Translate_while_recording()
        self.page.local_translate_while_recording_page.click_replace()
        self.page.local_translate_while_recording_page.click_confirm()
        for i in range(10):
            time.sleep(10)
            self.driver.press_keycode(26)
            self.driver.press_keycode(26)
            self.page.local_record_page.swipe_unlock()
            time.sleep(1)
            self.page.local_record_page.swipe_unlock()
            for i in range(4):
                self.page.local_record_page.click_enter_password_to_unlock()
            self.page.record_translate_while_recording_page.click_continue_transfer()
            self.page.record_page.click_save()
            self.page.record_page.click_save()









